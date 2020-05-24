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
Region = ['TwoEleDY']
TV = ['MedianLog10TrackAngle']
gROOT.ForceStyle(kTRUE)
	
#gStyle.SetOptStat(0)
for i in range(1):
	for j in range(1):
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
		pad1 = TPad("pad1", "The pad with the function",0,0.25,1,1)
		pad1.SetBottomMargin(0.04)
		pad1.SetLeftMargin(.12)
		pad1.SetRightMargin(.05)
		pad1.SetFrameLineWidth(3)
		
		
		pad1.Draw()
		c1.cd()
		pad2 = TPad("pad2", "The pad with the ratio plot",0,0,1,0.25)
		pad2.SetTopMargin(0.04)
		pad2.SetBottomMargin(0.4)
		pad2.SetLeftMargin(.12)
		pad2.SetRightMargin(.05)
		pad2.SetFrameLineWidth(3)
		pad2.SetGrid()
		pad2.Draw()
		c1.cd()
		Channel = Region[i]
		Var = TV[j]
		#_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/WHandLimit/analyzers/junk/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		#_file1 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/WHandLimit/analyzers/junk/Data_DoubleMu_G_%s_histograms.root' %Channel,'read')
		_file0 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc6_700_CMSSW_10_2_15/src/2018lldj/analyzers/junk/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/2018-LLDJ_slc6_700_CMSSW_10_2_15/src/2018lldj/analyzers/junk/Data_DoubleMuon_B_%s_histograms.root' %Channel,'read')
		h0=_file0.Get('h_%s_AllJets_AODCaloJet%s'%(Channel,Var))
		h1=_file1.Get('h_%s_AllJets_AODCaloJet%s'%(Channel,Var))
		#h = _file0.Get('h_TwoEleDY_AOD_elePt')
		#h0.SetTitle('DYJetsToLL_M-50 None,ISISO,All,All(.99 for all TrigSF) Dielectron Mass')
		pad1.cd()
		h0.SetTitle('Data&MC %s_%s Hist' %(Channel,Var))
		h0.GetXaxis().SetTitle('%s' %Var)
		h0.GetYaxis().SetTitle('Unit Integraled')
		h0.GetYaxis().SetTitleOffset(1.3)
		h0.Scale(1./h0.Integral())
		h0.SetLineColor(3)
		h0.Draw('HIST')
		h1.Scale(1./h1.Integral())
		h1.SetLineColor(4)
		h1.Draw('HIST SAME')
		h_ratio = h1.Clone('ratiohist')
		h_ratio.Divide(h0)
		#h_ratio.Scale(1./h_ratio.Integral())
		
		legend = TLegend(0.15,0.65,0.35,0.75) 		
   		legend.SetBorderSize(0)
    		legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
		legend.AddEntry(h0,"MC","l")
		legend.AddEntry(h1,"Data","l")
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
    		#extra2.DrawLatexNDC(0.55,0.91,"Run2 2016 Eras G,H       lumi 16.2/fb")
    		extra2.DrawLatexNDC(0.55,0.91,"Run2 2018       lumi 62.76/fb")

		pad2.cd()
		h_ratio.GetXaxis().SetTitle('%s' %Var)
		h_ratio.GetYaxis().SetTitle('Data/MC')
		h_ratio.GetYaxis().SetTitleSize(15)
		h_ratio.GetYaxis().SetTitleFont(43)
		h_ratio.GetYaxis().SetTitleOffset(2.5)
		h_ratio.GetYaxis().SetLabelFont(43)
		h_ratio.GetYaxis().SetLabelSize(10)
		#h_ratio.GetYaxis().SetNdivisions(-105)
		h_ratio.SetTitle('')
		h_ratio.GetXaxis().SetTitleSize(20)
		h_ratio.GetXaxis().SetTitleFont(43)
		h_ratio.GetXaxis().SetTitleOffset(4.0)
		h_ratio.GetXaxis().SetLabelFont(43)
		h_ratio.GetXaxis().SetLabelSize(20)
		h_ratio.SetMarkerStyle(20)
		h_ratio.SetMarkerColor(kBlue)
		h_ratio.SetMarkerSize(1)
		
		h_ratio.GetXaxis().SetRangeUser(-5,2)
		h_ratio.GetYaxis().SetRangeUser(0,2)
		h_ratio.Draw('hist ep')
		c1.Update()
		line = TLine(pad2.GetUxmin(),1.0,pad2.GetUxmax(),1.0)
		line.SetLineColor(kRed)
		line.SetLineWidth(3)
		line.SetLineStyle(9)
		line.Draw('')
		c1.Modified()
		c1.Update()
		c1.SaveAs('2018_%s_%s.png'%(Channel,Var))
		c1.Delete()
k=raw_input('Press ENTER to exit')
