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


Region = ['TwoMuOffZ']
#TV = ['AOD_daughterdR','AOD_jetScalardR','AOD_jetdaughterdR','AOD_ScalardaughterdR','AllJets_AODCaloJetMinDR']
#TV = ['AODCaloJetMedianLog10IPSig']
TV = ['AlphaMax']
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
		gPad.SetLogy()
		gStyle.SetOptStat(0)
		gStyle.SetLineWidth(3)
		gStyle.SetHistLineWidth(3)
		Channel = Region[i]
		Var = TV[j]
		#_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/Trackstudy/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/temproot/newEle.root','read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/temproot/newMu.root','read')
		h0=_file0.Get('h_TwoEleOffZ_AODCaloJetAlphaMax_1track')
		h1=_file0.Get('h_TwoEleOffZ_AODCaloJetAlphaMax_2track')
		h2=_file0.Get('h_TwoEleOffZ_AODCaloJetAlphaMax_5track')
		h3=_file0.Get('h_TwoEleOffZ_AODCaloJetAlphaMax_8track')
		h0.SetTitle('%s Hist' %Var)
		h0.GetXaxis().SetTitle('%s' %Var)
		h0.GetYaxis().SetTitle('Counts')
		h0.GetYaxis().SetTitleOffset(1.3)
		h0.Scale(117./60.)
		h0.SetLineColor(2)
		h0.Draw('HIST')
		#h0.GetYaxis().SetRangeUser(0.000001,0.3)
		h0.GetYaxis().SetRangeUser(0.1,1000000)
		h1.Scale(117./60.)
		h1.SetLineColor(1)
		h1.Draw('HIST SAME')
		h2.SetLineColor(3)
		h2.Scale(117./60.)
		h2.Draw('HIST SAME')
		h3.SetLineColor(4)
		h3.Scale(117./60.)
		h3.Draw('HIST SAME')
		
		legend = TLegend(0.50,0.35,0.85,0.55) 		
   		legend.SetBorderSize(0)
		legend.SetTextSize(.0175)
    		#legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"1track","l")
		legend.AddEntry(h1,"2track and above","l")
		legend.AddEntry(h2,"5track and above","l")
		legend.AddEntry(h3,"8track and above","l")
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
    		extra2.DrawLatexNDC(0.55,0.91,"Run2 DY tracks v. TagVars")
		c1.Modified()
		c1.Update()
		#k=raw_input('Press ENTER to exit')
		c1.SaveAs('Topology_%s_%s.pdf'%(Channel,Var))
k=raw_input('Press ENTER to exit')
