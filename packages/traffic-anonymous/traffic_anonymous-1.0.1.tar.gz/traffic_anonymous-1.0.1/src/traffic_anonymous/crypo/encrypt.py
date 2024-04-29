from cryptography.fernet import Fernet
from traffic_anonymous.myutils.utils import generate_aes_key, timestamp2time
import os
import csv
from tqdm import tqdm


class anon_flowlog:
    def __init__(self, srcdir, dstdir, key):
        self.srcdir = srcdir
        self.dstdir = dstdir
        self.key = generate_aes_key(key)

    def action(self):
        file_list = self.get_file_list()
        for file in file_list:
            flow_dir = os.path.join(self.dstdir, os.path.basename(file))
            os.makedirs(flow_dir, exist_ok=True)
            tcp_num = 0
            udp_num = 0
            with open(file, "r") as f:
                num_lines = sum(1 for line in f)  # 统计文件的行数
                f.seek(0)  # 重置文件指针到文件开头
                for i in tqdm(
                    range(num_lines), desc=f"handle {os.path.basename(file)}"
                ):
                    flow = f.readline()
                    tcp_num, udp_num = self.handle_flow(
                        flow, tcp_num, udp_num, flow_dir
                    )

    def get_file_list(self):
        file_list = []
        for filename in os.listdir(self.srcdir):
            filepath = os.path.join(self.srcdir, filename)
            if filename.isdigit() and os.path.isfile(filepath):
                file_list.append(filepath)
        return file_list

    def handle_flow(self, flow: str, tcp_num, udp_num, flow_dir):
        src = self.encrypt(flow.split("\t")[1].split(">")[0])
        dst = self.encrypt(flow.split("\t")[1].split(">")[1])
        if flow.split("\t")[2] == "6":
            tcp_num += 1
            self.save_csv(src, dst, "tcp", tcp_num, flow.split("\t")[-1], flow_dir)
        else:
            udp_num += 1
            self.save_csv(src, dst, "udp", udp_num, flow.split("\t")[-1], flow_dir)
        return tcp_num, udp_num

    # 加密函数
    def encrypt(self, ip_port):
        cipher_suite = Fernet(self.key)
        encrypted_ip_port = cipher_suite.encrypt(ip_port.encode())
        return encrypted_ip_port

    def save_csv(self, src, dst, pro, num, flow, flow_dir):
        # 首先将流转换为字典
        flow_dic = {"time": [], "length": []}
        packets = flow.split(";")[:-1]
        packets = [packet.split(",") for packet in packets]
        for packet in packets:
            flow_dic["time"].append(packet[2])
            if packet[0] == "1":
                length = int(packet[1])
            else:
                length = -1 * int(packet[1])

            flow_dic["length"].append(length)

        csv_file = os.path.join(flow_dir, pro + "_" + str(num) + ".csv")
        with open(csv_file, "w", newline="") as csvfile:
            fieldnames = flow_dic.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # 逐行写入数据
            for i in range(len(flow_dic["time"])):
                row_data = {key: flow_dic[key][i] for key in fieldnames}
                writer.writerow(row_data)

            # 写入表头
            writer.writeheader()
            src_dic = {"time": "src", "length": src}
            dst_dic = {"time": "dst", "length": dst}

            writer.writerow(src_dic)
            writer.writerow(dst_dic)


# # 解密函数
# def decrypt(encrypted_ip_port, key):
#     cipher_suite = Fernet(key)
#     decrypted_ip_port = cipher_suite.decrypt(encrypted_ip_port).decode()
#     return decrypted_ip_port


# # 示例
# def main():
#     # 生成密钥
#     key = generate_key()

#     print("密钥：", type(key))

#     # 待加密的源IP、源端口、目的IP和目的端口信息
#     ip_port_info = "192.168.1.100.8080"

#     # 加密
#     encrypted_ip_port_info = encrypt(ip_port_info, key)
#     print("加密后的信息：", encrypted_ip_port_info)

#     # 解密
#     decrypted_ip_port_info = decrypt(encrypted_ip_port_info, key)
#     print("解密后的信息：", decrypted_ip_port_info)
