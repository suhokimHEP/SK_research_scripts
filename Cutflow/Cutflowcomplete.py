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


Region = ['TwoEleZH']
label = ['None','TwoEle','GoodVtx','ZWindow','pTOSSF>10GeV','OneJet','N/A','N/A']
#Region = ['TwoMuDY']
gROOT.ForceStyle(kTRUE)
Var ='RawCutflow'	
#gStyle.SetOptStat(0)
for i in range(1):
		num = i
		c1 = TCanvas( 'c%s' %num, 'Histogram Drawing Options', 200, 400, 700, 900 )
		c1.SetGrid()
		gPad.SetLeftMargin(0.13)
		gPad.SetBottomMargin(0.12)
		gPad.SetTopMargin(0.12)
		gPad.SetTickx()
		gPad.SetTicky()
		gPad.SetLogy()
		gStyle.SetOptStat(0)
		gStyle.SetLineWidth(3)
		gStyle.SetHistLineWidth(3)
		Channel = Region[i]
		#_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/test/Data_DoubleEG_G_%s_histograms.root' %Channel,'read')
		_file1 = TFile.Open('/uscms/home/skim2/nobackup/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/roots/0721-original/Data_DoubleEG_B_%s_histograms.root' %Channel,'read')
		_file2 = TFile.Open('/uscms/home/skim2/nobackup/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/roots/0721-new/Data_DoubleEG_B_%s_histograms.root' %Channel,'read')
		#_file3 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc6_530_CMSSW_8_0_26_patch1/src/LLDJstandalones/roots/test/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		_file4 = TFile.Open('/uscms/home/skim2/nobackup/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/roots/0721-original/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		_file5 = TFile.Open('/uscms/home/skim2/nobackup/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/roots/0721-new/DYJetsToLL_M-50_%s_histograms.root' %Channel,'read')
		#h0=_file0.Get('h_%s_%s'%(Channel,Var))
		h1=_file1.Get('h_%s_%s'%(Channel,Var))
		h2=_file2.Get('h_%s_%s'%(Channel,Var))
		#h3=_file3.Get('h_%s_%s'%(Channel,Var))
		h4=_file4.Get('h_%s_%s'%(Channel,Var))
		h5=_file5.Get('h_%s_%s'%(Channel,Var))
		h1.SetTitle('DoubleEle TwoEle_%s Hist' %(Var))
		h1.GetXaxis().SetRangeUser(1,8)
		h1.GetYaxis().SetRangeUser(100,500000000)
		h1.GetYaxis().SetTitle('Counts')
		h1.GetYaxis().SetTitleOffset(1.3)
		h1.SetMarkerSize(1.5)
		h1.SetMarkerColor(2)
		h1.SetMarkerStyle(20)
		h1.Draw('P')
		h2.SetMarkerSize(1.5)
		h2.SetMarkerColor(3)
		h2.SetMarkerStyle(21)
		h2.Scale(4)
		h2.Draw('P SAME')
		h4.SetMarkerSize(1.5)
		h4.SetMarkerColor(4)
		h4.SetMarkerStyle(22)
		h4.Scale(0.125)
		#h4.Draw('P SAME')
		h5.SetMarkerSize(1.5)
		h5.SetMarkerColor(5)
		h5.SetMarkerStyle(23)
		h5.Scale(0.5)
		#h5.Draw('P SAME')
		for i in range (1,9):
			h1.GetXaxis().SetBinLabel(i+1,label[i-1])
		newlist, newlist2, newlist3, newlist4 = [],[],[],[]
	#	for i in range(1,9):
			#newlist.append(h0.GetBinContent(i))
			#newlist2.append(h1.GetBinContent(i))
			#newlist3.append(h2.GetBinContent(i))
			#newlist4.append(h3.GetBinContent(i))
			#newlist3.append(h2.GetBinContent(i))
		print(newlist)
		#print(newlist2)
		print(newlist3)
		#print(newlist4)
		#print(newlist3)
		legend = TLegend(0.70,0.65,0.95,0.75) 		
   		legend.SetBorderSize(0)
    		legend.SetNColumns(1)
    		legend.SetTextSize(0.015)
   		legend.SetFillColor(kWhite)
		#legend.AddEntry(h0,"Calo 16DoubleEG G","l")
		legend.AddEntry(h1,"Corr 17DoubleEG B","p")
		legend.AddEntry(h2,"Calo 17DoubleEG B","p")
		#legend.AddEntry(h3,"Calo 16DY50","l")
		#legend.AddEntry(h4,"Corr 17DY50","p")
		#legend.AddEntry(h5,"Calo 17DY50","p")
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
    		#extra2.DrawLatexNDC(0.55,0.91,"Full Run2        lumi 143/fb")
    		extra2.DrawLatexNDC(0.55,0.91,"Run2 #splitline{CaloJet 4.8/fb}{CorrJet 4.8/fb}")
		c1.Modified()
		c1.Update()
		c1.SaveAs('%s_%s.png'%(Channel,Var))
		c1.Delete()
k=raw_input('Press ENTER to exit')
