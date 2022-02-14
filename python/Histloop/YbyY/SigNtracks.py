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
TV = ['40DY','40WJets','40ST','15WJets','15ST','40TTJets']
#TV = ['AODCaloJetAlphaMax']
gROOT.ForceStyle(kTRUE)
	
for i in range(len(Region)):
	#for j in range(1):
	for j in range(len(TV)):
		num = i*j
		c1 = TCanvas( 'c%s' %num, 'Histogram Drawing Options', 0, 10, 700, 900 )
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
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/ControlRegionStudies/bin/ML/%s/WJetsToLNu.root' %Var,'read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/ControlRegionStudies/bin/ML/%s/DYJetsToLL_M-50.root' %Var,'read')
		_file2 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/ControlRegionStudies/bin/ML/%s/ST-Inclusive.root' %Var,'read')
		_file3 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/ControlRegionStudies/bin/ML/%s/TTJets.root' %Var,'read')
		_file4 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/ControlRegionStudies/bin/ML/%s/GluGluH_HToSSTo4Tau_MH-125_MS-15_ctauS-10.root' %Var,'read')
		_file5 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/ControlRegionStudies/bin/ML/%s/GluGluH_HToSSTo4Tau_MH-125_MS-40_ctauS-10.root' %Var,'read')
		_file6 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/ControlRegionStudies/bin/ML/%s/GluGluH_HToSSTo4Tau_MH-125_MS-55_ctauS-10.root' %Var,'read')

		h0=_file0.Get('Discriminator')
		h1=_file1.Get('Discriminator')
		h2=_file2.Get('Discriminator')
		h3=_file3.Get('Discriminator')
		h4=_file4.Get('Discriminator')
		h5=_file5.Get('Discriminator')
		h6=_file6.Get('Discriminator')
		h0.SetTitle('%s Training' %Var)
		h0.GetXaxis().SetTitle('ROI score')
		h0.GetYaxis().SetTitle('Unit Normalized')
		h0.GetYaxis().SetTitleOffset(1.3)
		h0.Scale(1./h0.Integral())
		h0.SetLineColor(1)
		h0.Draw('HIST')
		h0.GetYaxis().SetRangeUser(0.0001,0.6)

		h1.Scale(1./h1.Integral())
		h1.SetLineColor(2)
		h1.Draw('HIST SAME')
		h2.SetLineColor(3)
		h2.Scale(1./h2.Integral())
		h2.Draw('HIST SAME')
		h3.SetLineColor(4)
		h3.Scale(1./h3.Integral())
		h3.Draw('HIST SAME')
		h4.SetLineColor(5)
		h4.Scale(1./h4.Integral())
		h4.Draw('HIST SAME')
		h5.SetLineColor(6)
		h5.Scale(1./h5.Integral())
		h5.Draw('HIST SAME')
		h6.SetLineColor(7)
		h6.Scale(1./h6.Integral())
		h6.Draw('HIST SAME')
		
		legend = TLegend(0.65,0.75,0.85,0.87) 		
   		legend.SetBorderSize(0)
		legend.SetTextSize(.0175)
    		#legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"WJetsToLNu","l")
		legend.AddEntry(h1,"DYJetsToLL_M-50","l")
		legend.AddEntry(h2,"SingleTop","l")
		legend.AddEntry(h3,"TTJets","l")
		legend.AddEntry(h4,"ggH4#tau15GeV","l")
		legend.AddEntry(h5,"ggH4#tau40GeV","l")
		legend.AddEntry(h6,"ggH4#tau55GeV","l")
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
    		extra2.DrawLatexNDC(0.55,0.91,"Run2")
		c1.Modified()
		c1.Update()
		#k=raw_input('Press ENTER to exit')
		c1.SaveAs('Disc_%s.pdf'%Var)
k=raw_input('Press ENTER to exit')
