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
#TV = ['AOD_dilepton_Pt','AllJets_AODCaloJetPt','AllJets_AODCaloJetAlphaMax','AllJets_AODCaloJetMedianLog10IPSig','AllJets_AODCaloJetMedianLog10TrackAngle']
#TV = ['nSelectedAODCaloJet']
TV = ['AOD_dileptonNewB_Pt']
#TV = ['nSelectedAODCaloJetTag']
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
		#gPad.SetLogy()
		gStyle.SetOptStat(0)
		gStyle.SetLineWidth(3)
		gStyle.SetHistLineWidth(3)
		Channel = Region[i]
		Var = TV[j]
		#_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/OffZ/h125_llp20_ct100_%s_histograms.root' %Channel,'read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/OffZ/h150_llp50_ct100_%s_histograms.root' %Channel,'read')
		_file2 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/OffZ/h175_llp50_ct100_%s_histograms.root' %Channel,'read')
		_file3 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/OffZ/h200_llp50_ct100_%s_histograms.root' %Channel,'read')
		_file4 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/OffZ/h250_llp50_ct100_%s_histograms.root' %Channel,'read')
		_file5 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/analyzers/OffZ/h500_llp50_ct100_%s_histograms.root' %Channel,'read')
		#h0=_file0.Get('h_%s_%s'%(Channel,Var))
		h1=_file1.Get('h_%s_%s'%(Channel,Var))
		h2=_file2.Get('h_%s_%s'%(Channel,Var))
		h3=_file3.Get('h_%s_%s'%(Channel,Var))
		h4=_file4.Get('h_%s_%s'%(Channel,Var))
		h5=_file5.Get('h_%s_%s'%(Channel,Var))
		#h6=_file6.Get('h_%s_%s'%(Channel,Var))
		#h0.SetTitle('UnitNorm %s_%s Hist' %(Channel,Var))
		#h0.GetXaxis().SetTitle('%s' %Var)
		#h0.GetXaxis().SetRangeUser(0,400)
		#h0.GetYaxis().SetTitle('Counts')
		#h0.GetYaxis().SetTitleOffset(1.3)
		#h0.Scale(1./h0.Integral())
		#h0.SetLineColor(1)
		#h0.Draw('HIST')
		h1.SetTitle('UnitNorm %s_%s Hist' %(Channel,Var))
		h1.GetXaxis().SetTitle('%s' %Var)
		h1.GetYaxis().SetTitle('Counts')
		h1.GetYaxis().SetTitleOffset(1.3)
		h1.Scale(1./h1.Integral())
		h1.GetXaxis().SetRangeUser(0,300)
		#h1.GetYaxis().SetRangeUser(0,.8)
		h1.SetLineColor(2)
		h1.Draw('HIST')
		h2.Scale(1./h2.Integral())
		h2.SetLineColor(3)
		h2.Draw('HIST SAME')
		h3.Scale(1./h3.Integral())
		h3.SetLineColor(4)
		h3.Draw('HIST SAME')
		h4.Scale(1./h4.Integral())
		h4.SetLineColor(5)
		h4.Draw('HIST SAME')
		h5.Scale(1./h5.Integral())
		h5.SetLineColor(6)
		h5.Draw('HIST SAME')
		#h6.Scale(1./h6.Integral())
		#h6.SetLineColor(12)
		#h6.SetLineStyle(7)
		#h6.Draw('HIST SAME')
		
		legend = TLegend(0.55,0.65,0.85,0.85) 		
   		legend.SetTextSize(0.022)
   		legend.SetBorderSize(0)
    		legend.SetNColumns(2)
   		legend.SetFillColor(kWhite)
		#legend.AddEntry(h0,"#splitline{h125_llp20_}{ct100_Zdark}","l")
		legend.AddEntry(h1,"#splitline{h150_llp50_}{ct100_Zdark}","l")
		legend.AddEntry(h2,"#splitline{h175_llp50_}{ct100_Zdark}","l")
		legend.AddEntry(h3,"#splitline{h200_llp50_}{ct100_Zdark}","l")
		legend.AddEntry(h4,"#splitline{h250_llp50_}{ct100_Zdark}","l")
		legend.AddEntry(h5,"#splitline{h500_llp50_}{ct100_Zdark}","l")
		#legend.AddEntry(h6,"#splitline{ZH_MS55_}{ctau100}","l")
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
    		extra2.DrawLatexNDC(0.55,0.91,"Run2 Zdark")
		c1.Modified()
		c1.Update()
		k=raw_input('Press ENTER to exit')
		c1.SaveAs('Zdark_llp50_%s_%s.png'%(Channel,Var))
k=raw_input('Press ENTER to exit')
