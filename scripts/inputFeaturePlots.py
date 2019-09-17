import sys
import os
import optparse

parser = optparse.OptionParser()
parser.add_option("-o",dest="outfile",
    help = "path to output txt file with latex code")
parser.add_option("-p",dest="basepath",
    help = "basepath to plots relative to latex file",
    default = "figures/InputFeatures")
parser.add_option("-v",dest="variableset",
    help = "path to variable set of activated plots per jt region")
(opts, args) = parser.parse_args()

template = """
\\begin{{figure}}[h!]

{graphics}
    \\caption[input features]{{\\textbf{{Final selection of input features for the {jt} jet region before the fit to data.}} The predicted contributions of all background samples are stacked. the \\ttZ contribution is overlaid as a line scaled to match the integral of the total background. Ratios between data (black dots) and total background are shown in the bottom. The error bands correspond to the systematic uncertainties of the background contributions with a shape changing effect.
    }}
\\end{{figure}}
"""

graphtemplate = "\\includegraphics[width=0.45\\textwidth]{{{basepath}/ljets_{jt}_{varname}.pdf}}"

def translateJT(jt):
    if jt == "4j_ge3t": return "four"
    if jt == "5j_ge3t": return "five"
    if jt == "ge6j_ge3t": return "$\\geq 6$"
    else: return "NUMBEROFJETS"

sys.path.append(os.path.dirname(opts.variableset))
varset = __import__(os.path.basename(opts.variableset).replace(".py",""))


text = ""
for jt in args:
    varlist = varset.variables[jt]

    i = 1
    graphs = ""
    for v in varlist:
        graphs += graphtemplate.format(**{   
            "basepath": opts.basepath,
            "jt": jt,
            "varname": v.replace("[","_").replace("]","")
            })
        if i%2==0: graphs += "\\\\\n"
        graphs += "\n"
        if i == 6 or v == varlist[-1]:
            text += template.format(**{
                "graphics": graphs,
                "jt": translateJT(jt),
                })
            text += "\n\\newpage\n"
            graphs = ""
            i = 0
        i+=1

with open(opts.outfile, "w") as f:
    f.write(text)

