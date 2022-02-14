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
TV = ['NoPunzi']
gROOT.ForceStyle(kTRUE)
	
for i in range(len(Region)):
	for j in range(len(TV)):
		num = i*j
		c1 = TCanvas( 'c%s' %num, 'Histogram Drawing Options', 0, 10, 700, 600 )
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
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/NewDisctest/ggH_HToSSTo4Tau_MH-125_MS-15_ctauS-100_Usual.root','read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/NewDisctest/TTJets_Usual.root','read')
		_file2 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/NewDisctest/ST_s-channel_4f_hadronicDecays_Usual.root','read')
		_file3 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/WJetsToLNu_Usual.root','read')

		h0=_file0.Get('Discriminator')
		h1=_file1.Get('Discriminator')
		h2=_file2.Get('Discriminator')
		h3=_file3.Get('Discriminator')
		h0.GetXaxis().SetTitle('ROI score')
		h0.GetYaxis().SetTitle('Unit Normalized')
		h0.GetYaxis().SetTitleOffset(1.3)
		h0.Scale(1./h0.Integral())
		h0.SetLineColor(1)
		h0.Draw('HIST')
		h0.GetXaxis().SetRangeUser(0.0,1.0)
		h0.GetYaxis().SetRangeUser(0.00001,1.0)

		h1.Scale(1./h1.Integral())
		h1.SetLineColor(2)
		h1.Draw('HIST SAME')
		
		h2.Scale(1./h2.Integral())
		h2.SetLineColor(3)
		h2.Draw('HIST SAME')
		h3.Scale(1./h3.Integral())
		h3.SetLineColor(4)
		h3.Draw('HIST SAME')
		legend = TLegend(0.45,0.75,0.85,0.87) 		
   		legend.SetBorderSize(0)
		legend.SetTextSize(.0275)
    		#legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"Signal (MS,ctau)=(15GeV,100mm)","l")
		legend.AddEntry(h1,"TTJets","l")
		legend.AddEntry(h2,"SingleTop","l")
		legend.AddEntry(h3,"WJets","l")
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
		extra2.SetTextFont(62)
    		title.DrawTextNDC(0.2,0.91,"CMS")
    		extra.DrawTextNDC(0.3,0.91,"Preliminary")
    		extra2.DrawLatexNDC(0.55,0.91,"Run2 2018")
		c1.Modified()
		c1.Update()
		#k=raw_input('Press ENTER to exit')
		c1.SaveAs('Disc_%s.pdf'%Var)
k=raw_input('Press ENTER to exit')
