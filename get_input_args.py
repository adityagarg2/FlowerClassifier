import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('train.py', type = str, default = 'flowers')
    parser.add_argument('--arch', choices = ['vgg13', 'vgg16'], default = 'vgg16', help = 'Choose between torchvision architecture type: vgg16 and vgg13')
    parser.add_argument('--save_dir', type = str, default = '', help = 'Enter directory\'s path for saving \'checkpoint.pth\' file')
    parser.add_argument('--lr', type = float, default = 0.001, help = 'Enter learning rate for model. (Typiclaly between 10^-1 to 10^-6)')
    parser.add_argument('--hidden_units', type = int, default = 512, help = 'Enter number of hidden_units for the second last hidden layer.')
    parser.add_argument('--epocs', type = int, default = 3, help = 'Enter the number of epochs for which the model is to be trained (Avoid more than 5 due to large training time.) ')
    parser.add_argument('--gpu', action = 'store_true' , help = 'Only evoke if you want to use GPU for training')

    return parser.parse_args()
