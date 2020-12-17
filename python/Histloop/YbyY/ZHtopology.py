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
#TV = ['AOD_daughterdR','AOD_jetScalardR','AOD_jetdaughterdR','AOD_ScalardaughterdR','AllJets_AODCaloJetMinDR']
TV = ['AOD_ScalardR']
gROOT.ForceStyle(kTRUE)
	
for i in range(len(Region)):
	for j in range(len(TV)):
		num = i*j
		c1 = TCanvas( 'c%s' %num, 'Histogram Drawing Options', 200, 10, 700, 900 )
		c1.SetGrid()
		gPad.SetLeftMargin(0.13)
		gPad.SetBottomMargin(0.12)
		gPad.SetTickx()
		gPad.SetTicky()
		gStyle.SetOptStat(0)
		gStyle.SetLineWidth(3)
		gStyle.SetHistLineWidth(3)
		Channel = Region[i]
		Var = TV[j]
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/beamer/ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10_%s_histograms.root' %Channel,'read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/beamer/ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10_%s_histograms.root' %Channel,'read')
		_file2 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/beamer/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10_%s_histograms.root' %Channel,'read')
		_file3 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/beamer/ZH_HToSSTodddd_ZToLL_MH-125_MS-7_ctauS-10_%s_histograms.root' %Channel,'read')
		h0=_file0.Get('h_%s_%s'%(Channel,Var))
		h1=_file1.Get('h_%s_%s'%(Channel,Var))
		h2=_file2.Get('h_%s_%s'%(Channel,Var))
		h3=_file3.Get('h_%s_%s'%(Channel,Var))
		h0.SetTitle('%s Hist' %Var)
		h0.GetXaxis().SetTitle('%s' %Var)
		h0.GetYaxis().SetTitle('Counts')
		h0.GetYaxis().SetTitleOffset(1.3)
		h0.Scale(1./h0.Integral())
		h0.SetLineColor(2)
		h0.Draw('HIST')
		h0.GetYaxis().SetRangeUser(0,0.1)
		h1.Scale(1./h1.Integral())
		h1.SetLineColor(1)
		h1.Draw('HIST SAME')
		h2.SetLineColor(3)
		h2.Scale(1./h2.Integral())
		h2.Draw('HIST SAME')
		h3.SetLineColor(4)
		h3.Scale(1./h3.Integral())
		h3.Draw('HIST SAME')
		
		legend = TLegend(0.50,0.65,0.85,0.85) 		
   		legend.SetBorderSize(0)
		legend.SetTextSize(.0175)
    		#legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"Sig(H#rightarrow SS#rightarrow bbbb): M_{S}=15 c#tau_{S}=10","l")
		legend.AddEntry(h1,"Sig(H#rightarrow SS#rightarrow bbbb): M_{S}=40 c#tau_{S}=10","l")
		legend.AddEntry(h2,"Sig(H#rightarrow SS#rightarrow bbbb): M_{S}=55 c#tau_{S}=10","l")
		legend.AddEntry(h3,"Sig(H#rightarrow SS#rightarrow dddd): M_{S}=7 c#tau_{S}=10","l")
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
		extra2.SetTextSize(0.025)
		extra2.SetTextColor(kBlack)
		extra2.SetTextAlign(11)
		extra2.SetTextFont(62)
    		title.DrawTextNDC(0.2,0.91,"CMS")
    		extra.DrawTextNDC(0.3,0.91,"Preliminary")
    		extra2.DrawLatexNDC(0.55,0.91,"Run2 146/fb ZH signal topology")
		c1.Modified()
		c1.Update()
		#k=raw_input('Press ENTER to exit')
		c1.SaveAs('Topology_%s_%s.pdf'%(Channel,Var))
k=raw_input('Press ENTER to exit')
