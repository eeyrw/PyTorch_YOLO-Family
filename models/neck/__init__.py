from .spp import SPPBlock
from .dilated_encoder import DilatedEncoder
from ..basic.conv import ConvBlocks


def build_neck(model, in_ch, out_ch, act='lrelu'):
    if model == 'conv_blocks':
        print("Neck: ConvBlocks")
        neck = ConvBlocks(c1=in_ch, c2=out_ch, act=act)
    elif model == 'spp':
        print("Neck: SPP")
        neck = SPPBlock(c1=in_ch, c2=out_ch, act=act)
    elif model == 'dilated_encoder':
        print("Neck: Dilated Encoder")
        neck = DilatedEncoder(c1=in_ch, c2=out_ch, act=act)

    return neck
