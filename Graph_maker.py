#!/usr/bin/env python3
import numpy as np
import argparse
import yaml
import math
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib import ticker, colors
import seaborn as sns
from pylab import cm


class Const:

  @property
  def boltz_in_kcal(self) -> float:
    boltz_in_kcal=1.987204292510*10**(-3)
    return boltz_in_kcal


class Graph_maker:
  #####################################################################
  #####################################################################
  def __init__(self):
    return
  #####################################################################
  #####################################################################
  def test(self):
    print("Hello world")
    return
  #####################################################################
  #####################################################################
  def set_tex(self):
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.sans-serif": ["Computer Modern Roman"]})
    plt.rcParams['text.latex.preamble'] = r'\usepackage{braket,physics,bm}'
    plt.rcParams['axes.axisbelow'] = True
 
    return
  #####################################################################
  #####################################################################
  def set_plot(self,params=""):

    self.set_default_params(params)
    if(params["use_seaborn"]):
      sns.set()


    if(params["use_tex"]):
      self.set_tex()


    self.fig, self.ax = plt.subplots(figsize=(params["fig_sizex"],params["fig_sizey"]))

    self.ax.set_xlabel(params["xlabel"],fontsize=params["xlabel_size"])
    self.ax.set_ylabel(params["ylabel"],fontsize=params["ylabel_size"])

    self.ax.grid(linewidth=params["grid_width"],\
                 linestyle=params["grid_style"],color=params["grid_color"])

    self.ax.tick_params(axis="x",labelsize=params["xticks_size"])
    self.ax.tick_params(axis="y",labelsize=params["yticks_size"])

    self.ax.set_facecolor(params["background_color"])


    for ax_temp in ("top","bottom","right","left"):
      self.ax.spines[ax_temp].set_linewidth(params["spines"])



    

    return
  #####################################################################
  #####################################################################
  def perform_plot(self,params):
    

    if(params["plot_contourf"] or params["plot_contour"] or params["plot_colormesh"]):
      self.perform_plot_contour(params)
    else:
      for idata in range(len(params["input"])):
        self.perform_plot_line(params,idata)



    if(params["use_legend"]):
      plt.legend(fontsize=params["legend_size"],loc=params["legend_loc"]) #, bbox_to_anchor=(0.5, 1),frameon=True)


    self.set_range(params)

    if(params["xticks_width"] != "auto"):
      self.ax.set_xticks(np.arange(params["xticks_sta"],params["xticks_end"]+params["xticks_width"],params["xticks_width"]))

    if(params["yticks_width"] != "auto"):
      self.ax.set_yticks(np.arange(params["yticks_sta"],params["yticks_end"]+params["yticks_width"],params["yticks_width"]))

    if(params["square"]):
      self.ax.set_aspect(1.0/self.ax.get_data_ratio(), adjustable='box')

    if(params["draw_rectangle"]):
      width  = params["xend_rectangle"] -params["xsta_rectangle"]
      height = params["yend_rectangle"] -params["ysta_rectangle"]
      
      x = np.linspace(params["xsta_rectangle"],params["xend_rectangle"],101)
      y = np.zeros(101)
      y[:] = params["ysta_rectangle"]
      self.ax.plot(x,y,linewidth=params["box_linewidth"],color=params["box_edgecolor"])

      y[:] = params["yend_rectangle"]
      self.ax.plot(x,y,linewidth=params["box_linewidth"],color=params["box_edgecolor"])


      y = np.linspace(params["ysta_rectangle"],params["yend_rectangle"],101)
      x = np.zeros(101)
      x[:] = params["xsta_rectangle"]
      self.ax.plot(x,y,linewidth=params["box_linewidth"],color=params["box_edgecolor"])

      x[:] = params["xend_rectangle"]
      self.ax.plot(x,y,linewidth=params["box_linewidth"],color=params["box_edgecolor"])

      rectangle = patches.Rectangle(xy=(params["xsta_rectangle"], params["ysta_rectangle"]), \
                                    width=width, height=height, edgecolor=params["box_edgecolor"],\
                                    facecolor=params["box_facecolor"],alpha=params["box_alpha"])
      self.ax.add_patch(rectangle)




#    self.ax.set_xticks([-math.pi, -0.5*math.pi, 0, 0.5*math.pi , math.pi],[r'-$\pi$', r'-$\pi/2$','0', r'$\pi/2$', r'$\pi$'])
#    self.ax.set_yticks([-math.pi, -0.5*math.pi, 0, 0.5*math.pi , math.pi],[r'-$\pi$', r'-$\pi/2$','0', r'$\pi/2$', r'$\pi$'])
    self.fig.tight_layout()
    self.fig.savefig(params["output"],dpi=params["dpi"])

    return
  #####################################################################
  #####################################################################
  def set_default_params(self,params):

    params_list=[ ["fig_sizex",6],\
                  ["fig_sizey",4.5],\
                  ["use_tex",True],\
                  ["use_grid",True],\
                  ["grid_width",1],\
                  ["grid_style","dotted"],\
                  ["xlabel","$x$"],\
                  ["ylabel","$y$"],\
                  ["cblabel","$z$"],\
                  ["xlabel_size",20],\
                  ["ylabel_size",20],\
                  ["cblabelsize",20],\
                  ["xticks_size",16],\
                  ["yticks_size",16],\
                  ["cbtickssize",16],\
                  ["spines",1],\
                  ["linewidth",[2,2,2,2,2,2,2,2,2]],\
                  ["style",["line","line","line","line","line","line","line","line"]],\
                  ["linestyle",["solid","solid","solid","solid","solid","solid","solid","solid","solid","solid","solid","solid"]],\
                  ["legend",["","","","","","","","","","","","","","","",""]],\
                  ["use_legend",True],\
                  ["legend_size",10],\
                  ["legend_loc","best"],\
                  ["marker",["o","^","s","x","D"]],\
                  ["markersize",[0,0,0,0,0,0,0,0]],\
                  ["interval",[1,1,1,1,1,1,1,1]],\
                  ["marker_edge_width",[1,1,1,1,1,1,1,1]],\
                  ["color",['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']],\
                  ["marker_only_outline",[False,False,False,False,False,False,False]],\
                  ["xmin","auto"],\
                  ["xmax","auto"],\
                  ["ymin","auto"],\
                  ["ymax","auto"],\
                  ["xscale","linear"],\
                  ["yscale","linear"],\
                  ["cbscale","linear"],\
                  ["rho_to_PMF",False],\
                  ["set_bottom_zero",False],\
                  ["set_zero_point",False],\
                  ["point_to_be_zero",0.0],\
                  ["plot_contour",False],\
                  ["plot_contourf",False],\
                  ["plot_colormesh",False],\
                  ["square",False],\
                  ["contour_level","auto"],\
                  ["contourf_level","auto"],\
                  ["cbmin","auto"],\
                  ["cbmax","auto"],\
                  ["cmap","viridis"],\
                  ["use_seaborn",False],\
                  ["times_RT",False],\
                  ["temperature",""],\
                  ["xticks_width","auto"],\
                  ["xticks_sta","0"],\
                  ["xticks_end","1"],\
                  ["yticks_width","auto"],\
                  ["yticks_sta","0"],\
                  ["yticks_end","1"],\
                  ["draw_rectangle",False],\
                  ["xsta_rectangle",0.0],\
                  ["ysta_rectangle",0.0],\
                  ["xend_rectangle",1.0],\
                  ["yend_rectangle",1.0],\
                  ["box_linewidth",1.0],\
                  ["box_edgecolor","black"],\
                  ["box_facecolor","None"],\
                  ["box_alpha",0.0],\
                  ["background_color","white"],\
                  ["grid_color","gray"],\
                  ["cbar_width","auto"],\
                  ["cbar_sta","0"],\
                  ["cbar_end","1"],\
                  ["cbmin_contour","auto"],\
                  ["cbmax_contour","auto"],\
                  ["extend","neither"],\
                  ["set_extreme",False],\
                  ["extreme_under_color","black"],\
                  ["extreme_over_color","black"],\
                  ["dpi",500],\
                  ["rasterize",True]
                  ]

    for iparam in range(len(params_list)):
      try:
        dummy=params[params_list[iparam][0]]
      except KeyError:
        params[params_list[iparam][0]]=params_list[iparam][1]




    return
  #####################################################################
  #####################################################################
  def set_range(self,params):
#    if(params["xticks_width"] != "auto"):
#      self.ax.set_xticklabels(np.arange(params["xmin"],params["xmax"],params["xticks_width"]))

    if(params["xmin"]=="auto"):
      if(params["xmax"]=="auto"):
        pass
      else:
        self.pi_processor(params["xmax"])
        self.ax.set_xlim(right=params["xmax"])
    else:
      params["xmin"] = self.pi_processor(params["xmin"])
      if(params["xmax"]=="auto"):
        self.ax.set_xlim(left=params["xmin"])
      else:
        params["xmax"] = self.pi_processor(params["xmax"])
        self.ax.set_xlim([params["xmin"],params["xmax"]])





    if(params["ymin"]=="auto"):
      if(params["ymax"]=="auto"):
        pass
      else:
        self.pi_processor(params["ymax"])
        self.ax.set_ylim(top=params["ymax"])
    else:
      params["ymin"] = self.pi_processor(params["ymin"])
      if(params["ymax"]=="auto"):
        self.ax.set_ylim(bottom=params["ymin"])
      else:
        params["ymax"] = self.pi_processor(params["ymax"])
        self.ax.set_ylim([params["ymin"],params["ymax"]])

    self.ax.set_xscale(params["xscale"])
    self.ax.set_yscale(params["yscale"])

    return
  #####################################################################
  #####################################################################
  def pi_processor(self,value):
    if("pi" in str(value)):
      index_pi=value.find("pi")
      value=float(value[:index_pi])*math.pi
    else:
      pass
    return value
  #####################################################################
  #####################################################################
  def perform_plot_line(self,params,idata):

    data = np.loadtxt(params["input"][idata])
    x = data[:,0]
    y = data[:,1]

    if(params["rho_to_PMF"]):
      y_temp = y
      y = -np.log(y_temp)
#      y = y -np.min(y)
      if(params["times_RT"]):
        const = Const()
        if(params["temperature"]==""):
          print("To time RT, you have to write the temperarute")
        else:
          y = y*const.boltz_in_kcal*params["temperature"]

    if(params["set_bottom_zero"]):
      y = y -np.min(y)

    if(params["set_zero_point"]):
      index_to_be_zero = np.argmin(np.abs( x - params["point_to_be_zero"] ))
      y = y -y[index_to_be_zero]
      

    if(params["legend"][idata]==""):
      params["legend"][idata]=params["input"][idata]


    if(params["marker_only_outline"][idata]):
      marker_facecolor="None"
    else:
      marker_facecolor=params["color"][idata]

    self.ax.plot(x[::params["interval"][idata]],y[::params["interval"][idata]],\
                 linewidth=params["linewidth"][idata],\
                 linestyle=params["linestyle"][idata],\
                 label=params["legend"][idata],\
                 color=params["color"][idata],\
                 marker=params["marker"][idata],\
                 markersize=params["markersize"][idata],\
                 markeredgewidth=params["marker_edge_width"][idata],\
                 markerfacecolor=marker_facecolor,\
                 )



    return
  #####################################################################
  #####################################################################
  def perform_plot_contour(self,params):

    data = np.loadtxt(params["input"][0])
    x=data[:,0]
    y=data[:,1]
    z=data[:,2]
    x = np.unique(x)
    y = np.unique(y)


    Z = np.empty((len(y),len(x)))

    for i in range(len(x)):
      for j in range(len(y)):
        Z[j][i] = z[j+(i-1)*len(y)]

    if(params["rho_to_PMF"]):
      if(params["set_bottom_zero"]):
        Z = Z/np.max(Z)
      for i in range(len(x)):
        for j in range(len(y)):
          if(Z[j][i]>0):
            Z[j][i] = -np.log(Z[j][i])
          else:
            Z[j][i] = math.nan



    X, Y = np.meshgrid(x,y)

    if(params["contour_level"]=="auto"):
      params["contour_level"]=11


    if(params["contourf_level"]=="auto"):
      params["contourf_level"]=11



    cmap_use = plt.get_cmap(params["cmap"]).copy()
    if(params["set_extreme"]):
      cmap_use.set_extremes(under=params["extreme_under_color"],over=params["extreme_over_color"])
     
    

    if(params["plot_contourf"]):
      if(params["cbmin"]=="auto" and params["cbmax"]=="auto"):
        c = self.ax.contourf(X,Y,Z,levels=params["contourf_level"],cmap=cmap_use)
        if(params["plot_contour"]):
          self.ax.contour(X,Y,Z,levels=params["contour_level"],colors="black",linestyles="solid",linewidths=0.2)
        else:
          self.ax.contour(X,Y,Z,levels=params["contour_level"],linestyles="solid",cmap=cmap_use)

      else:
        c = self.ax.contourf(X,Y,Z,\
                            np.linspace(params["cbmin"],params["cbmax"],params["contourf_level"]),\
                            cmap=cmap_use,extend=params["extend"])
#        self.ax.contour(X,Y,Z,\
#                        np.linspace(params["cbmin"],params["cbmax"],params["contourf_level"]),\
#                        linestyles="solid",cmap=params["cmap"],linewidths=1)
        if(params["plot_contour"]):
          if(params["cbmin_contour"]=="auto"):
            self.ax.contour(X,Y,Z,\
                            np.linspace(params["cbmin"],params["cbmax"],params["contour_level"]),\
                            colors="black",linestyles="solid",linewidths=0.1)
          else:
            self.ax.contour(X,Y,Z,\
                            np.linspace(params["cbmin_contour"],params["cbmax_contour"],params["contour_level"]),\
                            colors="black",linestyles="solid",linewidths=0.1)

    elif(params["plot_colormesh"]):
      if(params["cbscale"]=="log"):
        c = self.ax.pcolormesh(X,Y,Z,norm=colors.LogNorm(),cmap=cmap_use,rasterized=params["rasterize"])
      else:
        c = self.ax.pcolormesh(X,Y,Z,cmap=cmap_use,rasterized=params["rasterize"])
      if(params["plot_contour"]):
        if(params["cbmin"]=="auto" and params["cbmax"]=="auto"):
          self.ax.contour(X,Y,Z,levels=params["contour_level"],colors="black",linestyles="solid",linewidths=0.1)
        else:
          self.ax.contour(X,Y,Z,\
                          np.linspace(params["cbmin"],params["cbmax"],params["contour_level"]),\
                          colors="k",linewidths=0.1)
          c.set_clim(vmin=params["cbmin"],vmax=params["cbmax"])
      else:
        if(params["cbmin"]=="auto" and params["cbmax"]=="auto"):
          pass
        else:
          c.set_clim(vmin=params["cbmin"],vmax=params["cbmax"])


      

    #plt.contour(X,Y,Z,np.linspace(cbmin,cbmax,contourf_level),cmap=cm.turbo)
#    plt.contour(X,Y,Z,np.linspace(cbmin,cbmax,contourf_level),colors="k",linewidths=1)

    cbar = self.fig.colorbar(c,extend=params["extend"])

    cbar.set_label(params["cblabel"],fontsize=params["cblabelsize"])
    cbar.ax.tick_params(labelsize=params["cbtickssize"])

    if(params["cbar_width"] != "auto"):
      cbar.set_ticks(np.arange(params["cbar_sta"],params["cbar_end"]+params["cbar_width"],params["cbar_width"]))

    self.set_range(params)





    return
  #####################################################################
  #####################################################################


def main():
  parser =  argparse.ArgumentParser(description='This program is intended for making graphs by matplotlib')
  parser.add_argument("--input",help="input yaml file",required=True)
  args = parser.parse_args()
  print("arguments:")
  print(args)
  input_yaml = args.input
  
  with open(input_yaml) as file:
    params = yaml.safe_load(file)

  print("###################################################")
  print("###################################################")
  print("Input params:")
  print(params)
  print("###################################################")
  print("###################################################")

  graph=Graph_maker()
  graph.set_plot(params)
  graph.perform_plot(params)


  print("###################################################")
  print("###################################################")
  print("Used params:")
  print(params)
  print("###################################################")
  print("###################################################")




if __name__=="__main__":
  main()


