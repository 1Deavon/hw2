# import the necessary packages
import os

# initialize the list of class label names
CLASSES = [
    "top",
    "trouser",
    "pullover",
    "dress",
    "coat",
    "sandal",
    "shirt",
    "sneaker",
    "bag",
    "ankle boot",
]

# define the minimum learning rate, maximum learning rate, batch size,
# step size, CLR method, and number of epochs
MIN_LR = 10e-9
MAX_LR = 10e1
BATCH_SIZE = 64
STEP_SIZE = 10
CLR_METHOD = "triangular"
NUM_EPOCHS = 5

# define the path to the output training history plot and cyclical
# learning rate plot
LRFIND_PLOT_PATH = os.path.sep.join(["output", "lrfind_plot.png"])
TRAINING_PLOT_PATH = os.path.sep.join(["output", "training_plot.png"])
CLR_PLOT_PATH = os.path.sep.join(["output", "clr_plot.png"])