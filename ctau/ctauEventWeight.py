## \author Wim Lavrijsen
from __future__ import division
#import ROOT
import glob
from ROOT import *
#from histutil import *
c1 = TCanvas( 'c1', 'Histogram Drawing Options', 800,800 )
c1.SetGrid()
gStyle.SetHistLineWidth(3)
gStyle.SetLineWidth(3)
gPad.SetTickx()
gPad.SetTicky()
#gPad.SetLogy()
gStyle.SetLineWidth(3)
gStyle.SetPalette(kBird)
gStyle.SetOptStat(1000111)
gStyle.SetStatW(0.18)
gStyle.SetStatH(0.18)
c1.Clear()
pad1 = TPad("pad1", "The pad with the function",0,0.25,1,1)
pad1.SetFrameLineWidth(3)


pad1.Draw()
c1.cd()
sample ='ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10 & 5'   
h16 = TH1F("Decaydist",'%s Decaydist' % sample,100, 0, 100)
h16w = TH1F("Decaydistw",'%s Decaydistw' % sample,100, 0, 100)
h16w.Sumw2()
h16s = TH1F("ctauEventWeight",'%s ctauEventWeight' % sample,80, 0, 4)
#DY16dir=glob.glob('/eos/uscms/store/group/lpchbb/LLDJntuples/SuhoKim_Ntuples/ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/crab_ZH_HToSSTobbbb_MS-15_ctauS-10/190516_043325/0000/*')
DY16dir=glob.glob('roots/*')
for i in range (7):
        filename = DY16dir[i]
        _file0 = TFile.Open(filename,'read')
	mytree16 = _file0.Get("lldjNtuple/EventTree")
	for entry in mytree16:
		ctau = mytree16.ctauEventWeight
		h16s.Fill(ctau[0],1)
		#print(ctau[0])	
		Decaydist=mytree16.AODnVtx
		h16.Fill(Decaydist,1)
		h16w.Fill(Decaydist,ctau[0])
		
		#Decaydist=mytree16.Decaydist
		#weight = mytree16.Simweight
		#number = Decaydist.size()
		#for i in range(number):
		#	#h16s.Fill(weight[i],1)
		#	h16.Fill(Decaydist[i],1)
		#	h16w.Fill(Decaydist[i],weight[i])
		
#error=0.
#IntError=h16w.IntegralAndError(1,h16w.GetNbinsX(),error,"")
#print(error)
h16w.Draw('HIST')
h16w.SetLineColor(4)
h16.Draw('HIST SAME')
#h16.Fit("expo")
#h16w.Fit("expo")
#h16.GetXaxis().SetRangeUser(0,10)
h16.GetXaxis().SetTitle("Decay distance in scalar frame")
h16w.GetYaxis().SetRangeUser(0,5000)
h16.SetLineColor(2)
#title = TPaveLabel(.11,.95,.35,.99,"new title","brNDC")
#title.Draw()
#g1 = TF1("m1","pol1",0,3)
#g2 = TF1("m2","pol1",0,3)
#h16w.Fit(g1)
#h16.Fit(g2)

str2='#int_{10mm} ='+str(h16.Integral())
str1='#int_{5mm} ='+str(h16w.Integral())
str3='Normalization = '+str(h16w.Integral()/h16.Integral())
legend = TLegend(0.5,0.75,0.7,0.9) 		
legend.AddEntry(h16,"Decaydist for c#tau =10mm","f")
legend.AddEntry(h16w,"Decaydist for c#tau =5mm","f")
legend.Draw()
fitbox = TPaveText(.3,.75,.5,.9,"brNDC")
fitbox.SetBorderSize(1)
fitbox.SetFillColor(0)
fitbox.AddText(str1)
fitbox.AddText(str2)
fitbox.AddText(str3)
fitbox.Draw()
l = TLatex()
l.SetTextAlign(13)
l.SetTextSize(0.02)
l.DrawLatexNDC(0.23,0.92,"CMS #it{Preliminary}                           Eras GH    16.2/fb  (13TeV)")
#l = TLatex()
#l2 = TLatex()
#l.SetTextAlign(33);
#l.SetTextSize(0.02)
#l2.SetTextWidth(1)
#l.DrawTextNDC(0.13,0.9,"CMS")
#l.DrawTextNDC(0.17,0.9,"#it{Preliminary}")
c1.Modified()
c1.Update()
c1.SaveAs("1w.png")








c2 = TCanvas( 'c2', 'Histogram Drawing Options', 800,800 )
gStyle.SetHistLineWidth(3)
gPad.SetTickx()
gPad.SetTicky()
h16s.Draw('HIST')
#h16s.Fit("expo")
h16s.SetTitle('EvenWeight for ctau 10mm->5mm')
h16s.GetXaxis().SetTitle('EventWeight')
l = TLatex()
l.SetTextAlign(13)
l.SetTextSize(0.02)
l.DrawLatexNDC(0.23,0.92,"CMS #it{Preliminary}                           Eras GH    16.2/fb  (13TeV)")
c2.Modified()
c2.Update()
c2.SaveAs("2w.png")



k=raw_input('Press ENTER to exit')
