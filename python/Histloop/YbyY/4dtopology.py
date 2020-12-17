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


Region = ['TwoEleOffZ']
#TV = ['AOD_ScalardR','AOD_daughterdR','AOD_jetScalardR','AOD_jetdaughterdR','AOD_ScalardaughterdR']
TV = ['AOD_daughterdR']
gROOT.ForceStyle(kTRUE)
	
for i in range(len(Region)):
	for j in range(len(TV)):
		num = i*j
		c1 = TCanvas( 'c%s' %num, 'Histogram Drawing Options', 200, 10, 700, 900 )
		#c1.SetGrid()
		gPad.SetLeftMargin(0.13)
		gPad.SetBottomMargin(0.12)
		gPad.SetTickx()
		gPad.SetTicky()
		gStyle.SetOptStat(0)
		gStyle.SetLineWidth(3)
		gStyle.SetHistLineWidth(3)
		Channel = Region[i]
		Var = TV[j]
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/4d/ZH_HToSSTodddd_ZToLL_MH-125_MS-7_ctauS-100_%s_histograms.root' %Channel,'read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/4d/ZH_HToSSTodddd_ZToLL_MH-125_MS-15_ctauS-100_%s_histograms.root' %Channel,'read')
		_file2 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/4d/ZH_HToSSTodddd_ZToLL_MH-125_MS-40_ctauS-100_%s_histograms.root' %Channel,'read')
		_file3 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/4d/ZH_HToSSTodddd_ZToLL_MH-125_MS-55_ctauS-100_%s_histograms.root' %Channel,'read')
		SdR0=_file0.Get('h_%s_%s'%(Channel,Var))
		SdR1=_file1.Get('h_%s_%s'%(Channel,Var))
		SdR2=_file2.Get('h_%s_%s'%(Channel,Var))
		SdR3=_file3.Get('h_%s_%s'%(Channel,Var))
		SdR0.SetMarkerSize(8)
		SdR0.GetXaxis().SetTitle("#Delta R")
		SdR0.GetYaxis().SetTitle("Events")
		SdR0.GetYaxis().SetTitleOffset(1.5)
		SdR0.Scale(1/SdR0.Integral())
		SdR0.SetLineColor(3)
		SdR0.Draw("HIST")
		SdR0.GetYaxis().SetRangeUser(0,.45)
		SdR1.Scale(1/SdR1.Integral())
		SdR1.SetLineColor(1)
		SdR1.Draw("HIST SAME")
		SdR2.Scale(1/SdR2.Integral())
		SdR2.SetLineColor(2)
		SdR2.Draw("HIST SAME")
		SdR3.Scale(1/SdR3.Integral())
		SdR3.SetLineColor(4)
		SdR3.Draw("HIST SAME")
		
		
		legend = TLegend(0.55,0.45,0.85,0.65) 		
		legend.SetTextSize(0.022)
		legend.SetBorderSize(0)
		legend.SetFillColor(kWhite)
		legend.AddEntry(SdR0,"m_{s} = 7GeV, c#tau=100mm","l")
		legend.AddEntry(SdR1,"m_{s} = 15GeV, c#tau=100mm","l")
		legend.AddEntry(SdR2,"m_{s} = 40GeV, c#tau=100mm","l")
		legend.AddEntry(SdR3,"m_{s} = 55GeV, c#tau=100mm","l")
		legend.Draw()
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
		title.DrawTextNDC(0.2,0.91,"CMS")
		extra.DrawTextNDC(0.3,0.91,"Preliminary")
		extra2.DrawLatexNDC(0.55,0.91,"Run2 13TeV")
		extra = TLatex(1,1,"") 
		extra.SetTextSize(0.03)
		extra.SetTextColor(kBlack)
		extra.SetTextFont(42)
		extra.DrawLatexNDC(0.48,0.78,"pp #rightarrow ZH #rightarrow Z (l^{+}l^{-})H(ss); s #rightarrow d#bar{d}")
		c1.Modified()
		c1.Update()
		c1.SaveAs("Zdark_llp20_dR100mm_v2.png")
		
		k=raw_input('Press ENTER to exit')
k=raw_input('Press ENTER to exit')
