from get_input_args import get_args

def main():

    in_args = get_args()
    arch = in_args.arch
    device = 'gpu' if in_args.gpu else 'cpu'
    lr = in_args.lr

    print(arch)
    print(device)
    print(lr)

main()
