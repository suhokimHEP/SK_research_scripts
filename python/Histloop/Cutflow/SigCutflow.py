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
import time

#Region = ['TwoEleZH','TwoMuZH']
Region = ['EleMuOSOF']
#label = ['None','PassLeptonSelection','GoodVtx','OneJet','LowpTOSOF&ZWindow']
label = ['None','PassLeptonSelection','GoodVtx','OneJet','pTOSOF&ZWindow']
#label = ['None','PassLeptonSelection','GoodVtx','ZWindow','LowPTOSSF','OneJet']
#label = ['None','PassLeptonSelection','GoodVtx','ZWindow','PTOSSF','OneJet']
#Region = ['TwoEleDY','TwoMuDY']
MassScale = ['15','40','55']
ctau = ['1','10','100','1000']
Var ='Cutflow'	
#gStyle.SetOptStat(0)
for j in range(len(MassScale)):
	for t in range(len(Region)):
		for k in range(len(ctau)):
			c1 = TCanvas( 'c%s', 'Histogram Drawing Options', 200, 400, 700, 900 )
			c1.SetGrid()
			gPad.SetLeftMargin(0.13)
			gPad.SetBottomMargin(0.12)
			gPad.SetTickx()
			gPad.SetTicky()
			gPad.SetLogy()
			gStyle.SetOptStat(0)
			gStyle.SetLineWidth(3)
			Channel = Region[t]
			MS = MassScale[j]
			dist = ctau[k]
			_file0 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/mine/roots/Preplots/ZH_HToSSTobbbb_ZToLL_MH-125_MS-%s_ctauS-%s_%s_histograms.root' %(MS,dist,Channel),'read')
			_file1 = TFile.Open('/uscms/home/skim2/nobackup/LLDJ_slc7_530_CMSSW_8_0_26_patch1/src/mine/roots/Preplots/ggZH_HToSSTobbbb_ZToLL_MH-125_MS-%s_ctauS-%s_%s_histograms.root' %(MS,dist,Channel),'read')
			#_file0 = TFile.Open('/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/analyzed/Systematics/ZH_HToSSTobbbb_ZToLL_MH-125_MS-%s_ctauS-%s_%s_histograms.root' %(MS,dist,Channel),'read')
			#_file1 = TFile.Open('/uscms/home/skim2/nobackup/2017-LLDJ_slc7_630_CMSSW_9_4_10/src/2017lldj/analyzers/exp/Data_DoubleEG_B_%s_histograms.root' %Channel,'read')
			h0=_file0.Get('h_%s_%s'%(Channel,Var))
			h1=_file1.Get('h_%s_%s'%(Channel,Var))
			h0.Add(h1)
			h0.SetTitle('%s:%s MS-%sc#tau_{s}%s' %(Channel,Var,MS,dist))
			#h0.GetYaxis().SetRangeUser(3,500)
			h0.SetMaximum(500)
			h0.SetLineWidth(2)
			h0.SetLineColor(1)
			h0.GetYaxis().SetMoreLogLabels()
			h0.GetYaxis().SetNoExponent()
			h0.GetYaxis().SetTitle('Events')
			h0.GetYaxis().SetTitleOffset(1.35)
			#h0.SetMarkerSize(0.5)
			#h0.SetMarkerColor(1)
			#h0.SetMarkerStyle(21)
			h0.Draw('ep')
			#h1.SetMarkerSize(1.5)
			#h1.SetMarkerColor(3)
			#h1.SetMarkerStyle(22)
			#h1.Draw('P SAME')
			for i in range (1,6):
				h0.GetXaxis().SetBinLabel(i+1,label[i-1])
			newlist, newlist2, newlist3 = [],[],[]
			for i in range(1,6):
				newlist.append(h0.GetBinContent(i+1))
				#newlist2.append(h1.GetBinContent(i))
			print(newlist)
			#print(newlist2)
			#legend = TLegend(0.75,0.65,0.95,0.75) 		
   			#legend.SetBorderSize(0)
    			#legend.SetNColumns(2)
   			#legend.SetFillColor(kWhite)
			#legend.AddEntry(h0,"16","p")
			#legend.AddEntry(h1,"17","p")
			#legend.AddEntry(h2,"18","p")
			#legend.Draw()
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
    			extra2.DrawLatexNDC(0.55,0.91,"2016 Eras GH     16.2/fb(13TeV)")

			c1.Modified()
			c1.Update()
			time.sleep(15)
			c1.SaveAs('CF_%s_MS%sctau%s.png'%(Channel,MS,dist))
k=raw_input('Press ENTER to exit')
