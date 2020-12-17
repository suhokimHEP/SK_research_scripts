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


Region = ['TwoEleOffZ','TwoMuOffZ']
#TV = ['AOD_daughterdR','AOD_jetScalardR','AOD_jetdaughterdR','AOD_ScalardaughterdR','AllJets_AODCaloJetMinDR']
#TV = ['AllJets_AODCaloJetNMatchedTracks','AllTags_AODCaloJetTagNMatchedTracks']
#TV = ['AllJets_AODCaloJetNMatchedTracks','AllTags_AODCaloJetTagNMatchedTracks']
#TV = ['AllJets_AODCaloJet_emEnergyFraction','AllTags_AODCaloJetTag_less3_emEnergyFraction','AllTags_AODCaloJetTag_emEnergyFraction']
#TV = ['AllJets_AODCaloJet_energyFractionHadronic','AllTags_AODCaloJetTag_less3_energyFractionHadronic','AllTags_AODCaloJetTag_energyFractionHadronic']
TV = ['emFraction-Over-HadronicFrction']
#TV = ['AODCaloJetAlphaMax']
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
		#gPad.SetLogy()
		gStyle.SetOptStat(0)
		gStyle.SetLineWidth(3)
		gStyle.SetHistLineWidth(3)
		Channel = Region[i]
		Var = TV[j]
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/SK_research_scripts/temp/temproot/new%s_DYJetsToLL_M-50_Vgamma.root' %Channel,'read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/SK_research_scripts/temp/temproot/new%s_ZGTo2LG_Vgamma.root' %Channel,'read')
		_file2 = TFile.Open('/uscms/home/skim2/nobackup/SK_research_scripts/temp/temproot/new%s_ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100_Vgamma.root' %Channel,'read')
		#_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/Vgamma/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		#_file1 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/Vgamma/ZGTo2LG_%s_histograms.root' %Channel,'read')
		#_file0 = TFile.Open('/uscms/home/skim2/nobackup/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/roots/Vgamma/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		#_file1 = TFile.Open('/uscms/home/skim2/nobackup/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/roots/Vgamma/ZGTo2LG_%s_histograms.root' %Channel,'read')
		#_file0 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/roots/Vgamma/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		#_file1 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/roots/Vgamma/ZGTo2LG_%s_histograms.root' %Channel,'read')
		h3=_file0.Get('h_%s_AllTags_AODCaloJetTag_energyFractionHadronic' % Channel)
		h4=_file1.Get('h_%s_AllTags_AODCaloJetTag_energyFractionHadronic' % Channel)
		h5=_file2.Get('h_%s_AllTags_AODCaloJetTag_energyFractionHadronic' % Channel)
		h0=_file0.Get('h_%s_AllTags_AODCaloJetTag_emEnergyFraction' % Channel)
		h1=_file1.Get('h_%s_AllTags_AODCaloJetTag_emEnergyFraction' % Channel)
		h2=_file2.Get('h_%s_AllTags_AODCaloJetTag_emEnergyFraction' % Channel)
		h0.Scale(1./h0.Integral())
		h1.Scale(1./h1.Integral())
		h2.Scale(1./h2.Integral())
		h3.Scale(1./h3.Integral())
		h4.Scale(1./h4.Integral())
		h5.Scale(1./h5.Integral())
		h0.Divide(h3)
		h1.Divide(h4)
		h2.Divide(h5)
		h0.SetTitle('%s Hist' %Var)
		h0.GetXaxis().SetTitle('%s' %Var)
		h0.GetYaxis().SetTitle('Counts')
		h0.GetYaxis().SetTitleOffset(1.3)
		#h0.Scale(1./h0.Integral())
		h0.SetLineColor(2)
		h0.Draw('HIST')
		#h0.GetYaxis().SetRangeUser(0.000001,0.4)
		h0.GetYaxis().SetRangeUser(0.000001,70)
		#h1.Scale(1./h1.Integral())
		h1.SetLineColor(1)
		h1.Draw('HIST SAME')
		#h2.Scale(1./h2.Integral())
		h2.SetLineColor(4)
		h2.Draw('HIST SAME')
		
		legend = TLegend(0.15,0.75,0.35,0.87) 		
   		legend.SetBorderSize(0)
		legend.SetTextSize(.0175)
    		#legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"DY","l")
		legend.AddEntry(h1,"ZGamma","l")
		legend.AddEntry(h2,"ZHMS15ct100","l")
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
    		extra2.DrawLatexNDC(0.55,0.91,"Run2 17,18")
		c1.Modified()
		c1.Update()
		#k=raw_input('Press ENTER to exit')
		c1.SaveAs('Ntrack_%s_%s.pdf'%(Channel,Var))
k=raw_input('Press ENTER to exit')
