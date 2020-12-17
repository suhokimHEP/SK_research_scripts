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


#Region = ['TwoEleDY','TwoMuDY']
Region = ['TwoMuOffZ']
TV = ['AllJets_AODCaloJetAlphaMax','AllJets_AODCaloJetMedianLog10TrackAngle','AllJets_AODCaloJetMedianLog10IPSig']
#TV = ['AllJets_AODCaloJetMedianLog10TrackAngle','AllJets_AODCaloJetMedianLog10IPSig']
#TV = ['AllJets_AODCaloJetAlphaMax']
#TV = ['MedianLog10TrackAngle','MedianLog10IPSig']
#TV = ['AOD_dilepton_Pt']
gROOT.ForceStyle(kTRUE)
	
#gStyle.SetOptStat(0)
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
		#_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/Final_Comparison/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		#_file0 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/roots/withZpt_noShift_noJet_newbin_InclusiveZ/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_%s_histograms.root' %Channel,'read')
		#_file1 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/roots/withZpt_noShift_noJet_newbin_JEC_InclusiveZ/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_%s_histograms.root' %Channel,'read')
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/NoJEC/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
	        _file1 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/JEC/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		#_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/junk/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TwoMuZH_histograms.root','read')
		#_file1 = TFile.Open('/uscms/home/skim2/nobackup/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/analyzers/junk/Data_DoubleEG_C_%s_histograms.root' %Channel,'read')
		#_file2 = TFile.Open('/uscms/home/skim2/nobackup/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/analyzers/junk2/Data_DoubleEG_C_%s_histograms.root' %Channel,'read')
		#_file1 = TFile.Open('/uscms/home/skim2/nobackup/2017-LLDJ_slc7_630_CMSSW_9_4_12/src/2017lldj/analyzers/junk/SUSY_100_TwoMuZH_histograms.root','read')
		h0=_file0.Get('h_%s_%s'%(Channel,Var))
		h1=_file1.Get('h_%s_%s'%(Channel,Var))
		#h2=_file2.Get('h_%s_AllJets_AODCaloJet%s'%(Channel,Var))
		#h1=_file1.Get('h_TwoEleDY_AllJets_AODCaloJet%s'%Var)
		#h0=_file0.Get('h_%s_%s'%(Channel,Var))
		#h1=_file1.Get('h_%s_%s'%(Channel,Var))
		#h2=_file2.Get('h_%s_%s'%(Channel,Var))
		h1.SetTitle('%s_%s Hist' %(Channel,Var))
		h1.GetXaxis().SetTitle('%s' %Var)
		h1.GetYaxis().SetTitle('Counts')
		h1.GetYaxis().SetTitleOffset(1.3)
		#h1.Scale(1./h1.Integral())
		#h1.Scale(9.)
		h1.SetLineColor(2)
		h1.Draw('HIST')
#		h0.GetYaxis().SetRangeUser(0,.3)
		#h0.Scale(1./h0.Integral())
		h0.SetLineColor(1)
		h0.Draw('HIST SAME')
		
		legend = TLegend(0.65,0.65,0.85,0.75) 		
   		legend.SetBorderSize(0)
    		legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"NoJEC","l")
		legend.AddEntry(h1,"JEC","l")
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
		extra2.SetTextSize(0.025)
		extra2.SetTextColor(kBlack)
		extra2.SetTextAlign(11)
		extra2.SetTextFont(62)
    		title.DrawTextNDC(0.2,0.91,"CMS")
    		extra.DrawTextNDC(0.3,0.91,"Preliminary")
    		extra2.DrawLatexNDC(0.55,0.91,"2018 No JEC v. JEC")
		c1.Modified()
		c1.Update()
		k=raw_input('Press ENTER to exit')
		c1.SaveAs('DY50_JEC_%s_%s.png'%(Channel,Var))
k=raw_input('Press ENTER to exit')
