from traffic_anonymous.myutils.utils import (
    generate_aes_key,
    IpdotPort2Ip_Port,
)
import os
from cryptography.fernet import Fernet
from tqdm import tqdm


class disanon_flowlog:
    def __init__(self, srcdir, dstdir, key):
        self.srcdir = srcdir
        self.dstdir = dstdir
        self.key = generate_aes_key(key)

    def action(self):
        dir_list = self.get_dir_list()
        for dir in dir_list:
            flow_dir = os.path.join(self.dstdir, os.path.basename(dir))
            os.makedirs(flow_dir, exist_ok=True)
            file_list = self.get_file_list(dir)
            num = 0
            for file in tqdm(
                file_list, desc=f"正在对{os.path.basename(dir)}的数据去匿名化"
            ):
                num += 1
                with open(file, "r") as f:
                    flowlog = f.readlines()
                    src = IpdotPort2Ip_Port(
                        self.decrypt(flowlog[-2].split(",")[-1].split("'")[-2])
                    )
                    dst = IpdotPort2Ip_Port(
                        self.decrypt(flowlog[-1].split(",")[-1].split("'")[-2])
                    )
                    flowlog = flowlog[:-2]
                output_name = (
                    "IIE_OTHER_"
                    + os.path.basename(file).split("_")[0]
                    + "_"
                    + src
                    + "_"
                    + dst
                    + "_"
                    + str(num)
                    + ".csv"
                )
                output_path = os.path.join(flow_dir, output_name)
                with open(output_path, "w") as f:
                    f.writelines(flowlog)

    def get_dir_list(self):
        file_list = []
        for filename in os.listdir(self.srcdir):
            filepath = os.path.join(self.srcdir, filename)
            if filename.isdigit() and os.path.isdir(filepath):
                file_list.append(filepath)
        return file_list

    def get_file_list(self, dir):
        all_files = []

        for root, directories, files in os.walk(dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                all_files.append(file_path)
        return all_files

    # 解密函数
    def decrypt(self, ip_port):
        cipher_suite = Fernet(self.key)
        decrypted_ip_port = cipher_suite.decrypt(ip_port).decode()
        return decrypted_ip_port


if __name__ == "__main__":
    aa = disanon_flowlog("../data/flowlog", "./", "iie12345")
    aa.action()
