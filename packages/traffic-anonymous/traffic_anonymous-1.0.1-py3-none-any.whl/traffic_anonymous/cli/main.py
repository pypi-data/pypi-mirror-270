import click
import sys

sys.path.append("/home/aimafan/Documents/mycode/traffic_anonymous/src")
import traffic_anonymous
from traffic_anonymous.myutils.logger import logger
from traffic_anonymous.crypo.encrypt import anon_flowlog
from traffic_anonymous.crypo.decrypt import disanon_flowlog


@click.group(invoke_without_command=True)
@click.pass_context
@click.option(
    "--version",
    "show_version",
    is_flag=True,
    help="Show traffic anonymous version and exit.",
)
def main(ctx, show_version):
    if show_version:
        print(f"traffic-anonymous version: " f"{traffic_anonymous.__version__}")
        sys.exit()


@main.command(name="encrypt")
@click.pass_context
@click.option(
    "--key",
    "-k",
    "key_seed",
    required=True,
    type=str,
    help="加密密钥",
    default="iie12345",
)
@click.option(
    "--srcdir",
    "-sd",
    "srcdir",
    required=True,
    type=str,
    help="流日志所在目录",
)
@click.option(
    "--dstdir",
    "-dd",
    "dstdir",
    required=True,
    type=str,
    help="匿名化之后输出的目录",
    default="./",
)
def encrypt(ctx, srcdir, dstdir, key_seed):
    """对流日志进行匿名化操作"""
    a = anon_flowlog(srcdir, dstdir, key_seed)
    a.action()


@main.command(name="decrypt")
@click.pass_context
@click.option(
    "--key",
    "-k",
    "key_seed",
    required=True,
    type=str,
    help="解密",
    default="iie12345",
)
@click.option(
    "--srcdir",
    "-sd",
    "srcdir",
    required=True,
    type=str,
    help="加密的数据所在路径",
)
@click.option(
    "--dstdir",
    "-dd",
    "dstdir",
    required=True,
    type=str,
    help="输出目录",
    default="./",
)
def decrypt(ctx, srcdir, dstdir, key_seed):
    """对匿名化之后的流日志进行去匿名化操作"""
    a = disanon_flowlog(srcdir, dstdir, key_seed)
    a.action()


if __name__ == "__main__":
    main()
