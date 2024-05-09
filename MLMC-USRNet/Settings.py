import datetime
import os

def parameters_setting(conf, args, method, filename):

    model_name = "MLMC"

    conf.I_loop_x = 5  # for meta learning
    conf.I_loop_k = 3  # hyper-parameters
    conf.D_loop = 5 # for MCMC sampling

    # iteration setting
    max_iterations = 1000 // conf.I_loop_x       # if MLMC->800/1000  if Non-Gaussian Kernel ->400
    conf.kernel_first_iteration = 200      # kernel network warm-up, default = 200
    conf.SSIM_iterations = 80 // conf.I_loop_x  # default = 80

    conf.Print_iteration = max_iterations * conf.I_loop_x // 5
    conf.max_iters = max_iterations

    # kernel setting
    conf.kernel_type = "Gaussian"           # choosing kernel type, Gaussian/motion/motion_line
    conf.MLMC_kp_lr = 1e-4                # kernel network learning rate, default = 1.5e-4

    conf.var_min_add = 3+(int(args.sf)-4)        # adding Gaussian variance, default = 0
    conf.var_max_add = 10+(int(args.sf)-4)       # adding Gaussian variance, default = 0
    conf.jj = 3                             # choosing motion kernel type
    conf.jj_kl = 0.1
    conf.kernel_x = (int(args.sf) + 1) * 3 / 2
    conf.kernel_x = (int(args.sf) + 1) * 3 / 2
    conf.kernel_y = conf.kernel_x


    # noise setting
    grad_loss_lr = 0.001

    # grad_loss_lr = 0
    print('grad_loss_lr:{}'.format(grad_loss_lr))

    conf.grad_loss_lr = grad_loss_lr
    conf.noise_estimator = "iid"  # "iid" or "niid" or "no-noise"
    conf.Image_disturbance = 0 / 255
    # conf.Net_disturbance = 0   # 0.001

    # output file name
    if args.SR:
        output_name = "{}_{}+USRNet".format(args.sf, method)
    else:
        output_name = "{}_{}".format(args.sf, method)

    # overwritting paths

    args.hr_dir = '../data/datasets/{}/HR'.format(args.dataset)
    args.output_dir = '../data/log_MLMC/{}_{}_lr_x{}'.format(args.dataset, model_name, output_name)
    conf.input_dir = args.input_dir
    conf.output_dir_path = os.path.abspath(args.output_dir)

    if not os.path.isdir(args.output_dir):
        os.makedirs(args.output_dir)

    if conf.kernel_type == "motion":
        motion_blur_path = '../data/datasets/motion_kernel_j{}_x{}/'.format(conf.jj, args.sf)
    elif conf.kernel_type == "motion_line":
        motion_blur_path = '../data/datasets/kernel_line_motion/'
    else:
        motion_blur_path = None
    conf.motion_blur_path = motion_blur_path

    # flag setting

    conf.IF_print = False
    conf.IF_DIV2K = False
    conf.model_num = output_name
    conf.filename = filename
    conf.method = method

    return conf, args












