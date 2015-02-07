from utils import filename
from utils.plots_helper import sensors 
import matplotlib
from matplotlib import pyplot
from matplotlib.backends.backend_pdf import PdfPages

make,fname = filename("sensor-plots.pdf")
dfile = "../datasets/real/intel/sensors-1000-dirty.txt"

# e, p, t, y, x
args = [
    (0.7,1,0.05,0,1),
    (0.7,1,0.05,0,3),
    (0,1,0.005,0,1)]

pdf = PdfPages(fname)
for (e,p,t,y,x) in args:
    title = "Outliers in Sensor Data\n"+str(p)+" Gaussians,$\\theta$=" + str(t)
    ofile = "../results/sensors_dirty_stat" + str(e) + "_mix" + str(p) + "_" + str(t) + ".out"
    sensors(title,x,y,dfile,ofile)
    pyplot.savefig(pdf, format = 'pdf', transparent = True)
    pyplot.clf()
pdf.close()
