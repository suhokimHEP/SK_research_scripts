## \file
## \ingroup tutorial_pyroot
## \notebook -js
## A Simple histogram drawing example
##
## \macro_image
## \macro_output
## \macro_code
##
## \author Wim Lavrijsen

from __future__ import division
from ROOT import *


Region = ['TwoEleDY']
TV = ['AOD_elePt']

gROOT.ForceStyle(kTRUE)
	
#gStyle.SetOptStat(0)
for i in range(len(Region)):
	for j in range(len(TV)):
		num = i*j
		c1 = TCanvas( 'c%s' %num, 'Histogram Drawing Options', 200, 600, 700, 900 )
		c1.SetGrid()
		pad1 = TPad("pad1","The pad with the function",0.01,0.01,0.99,0.99);
 		pad1.Draw()
		gPad.SetLeftMargin(0.13)
		gPad.SetBottomMargin(0.12)
		gPad.SetTopMargin(0.12)
		gPad.SetTickx()
		gPad.SetTicky()
		gStyle.SetOptStat(0)
		gStyle.SetLineWidth(3)
		gStyle.SetHistLineWidth(2)
		Channel = Region[i]
		Var = TV[j]
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/None/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/ID/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		_file2 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/IDISO/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		_file3 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/All/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		h0=_file0.Get('h_%s_%s'%(Channel,Var))
		h1=_file1.Get('h_%s_%s'%(Channel,Var))
		h2=_file2.Get('h_%s_%s'%(Channel,Var))
		h3=_file3.Get('h_%s_%s'%(Channel,Var))
		realregion = Channel
		h0.SetTitle('%s_%s Hist'%(realregion,Var))
		h0.GetXaxis().SetTitle('%s' %Var)
		h0.GetXaxis().SetRangeUser(0,150)

		h0.GetYaxis().SetTitle('Counts')
		h0.GetYaxis().SetTitleOffset(1.3)
		h0.SetLineColor(1)
		h0.Draw('HIST')
		h1.SetLineColor(2)
		h1.Draw('HIST SAME')
		#h2.SetLineColor(3)
		#h2.Draw('HIST SAME')
		h3.SetLineColor(4)
		h3.Draw('HIST SAME')
		legend = TLegend(0.65,0.50,0.90,0.85) 		
   		legend.SetBorderSize(0)
   		legend.SetTextSize(0.023)
    		#legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"#splitline{DYJetsToLL_M-50}{No SF}","l")
		legend.AddEntry(h1,"ID SF","l")
		#legend.AddEntry(h2,"ID/ISO SF","l")
		legend.AddEntry(h3,"ID/ISO/Trig SF","l")
		legend.Draw()
		#l = TLatex()
		#l.SetTextAlign(13)
		#l.SetTextSize(0.02)
		#l.DrawLatexNDC(0.23,0.92,"CMS #it{Preliminary}           2017 DataSet B,2018 DataSet C  (13TeV)")
		#l.DrawLatexNDC(0.23,0.62,"splitline{CMS #it{Preliminary}}{2016,2017,2018 full lumi}")
		title = TText(1,1,"") 
		title.SetTextSize(0.045)
		title.SetTextColor(kBlack)
		title.SetTextAlign(11)
		title.SetTextFont(62)
		
		extra = TText(1,1,"") 
		extra.SetTextSize(0.03)
		extra.SetTextColor(kBlack)
		extra.SetTextAlign(11)
		extra.SetTextFont(52)
		
		extra2 = TLatex(1,1,"") 
		extra2.SetTextSize(0.03)
		extra2.SetTextColor(kBlack)
		extra2.SetTextAlign(11)
		extra2.SetTextFont(42)
    		title.DrawTextNDC(0.2,0.89,"CMS")
    		extra.DrawTextNDC(0.3,0.89,"Preliminary")
    		extra2.DrawLatexNDC(0.55,0.89,"2016 lumi 16.2/fb (13 TeV)")
#		c1.Modified()
	#	c1.Update()

		#c1.Delete()
		k=raw_input('Press ENTER to exit')
		c1.SaveAs('%s_%s.pdf'%(realregion,Var))
k=raw_input('Press ENTER to exit')
