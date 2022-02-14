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


gROOT.ForceStyle(kTRUE)
	
c1 = TCanvas( 'c%s', 'Histogram Drawing Options', 0, 10, 700, 600 )
c1.SetGrid()
gPad.SetLeftMargin(0.13)
gPad.SetBottomMargin(0.12)
gPad.SetTickx()
gPad.SetTicky()
#gPad.SetLogy()
#gStyle.SetOptStat(0)
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
temp=[]
_file0 = TFile.Open('dosemap_output_startup_4forall.root','read')
hE = TH1F("1D_Signal","startupAll4mm2_SignalDispersion", 100, 0, 100)
for i in range(8,21):
	#print("Layer")
	#print(i)
	h0=_file0.Get('plotter/s_lay%d_ieta'%i)
	for j in range(h0.GetNbinsX()):
		#print("Binnum:%d"%j)
		#print(h0.GetBinContent(j+1))
		signal  = h0.GetBinContent(j+1)
		if(signal>0):
			hE.Fill(signal,576.0)
			temp.append(signal)


minval = min(temp)
minval = round(minval,5)
maxval = max(temp)
maxval = round(maxval,5)
print(minval)
print(maxval)
hE.GetXaxis().SetTitle('<S>pe')
hE.GetYaxis().SetTitle('#ofTiles')
hE.GetYaxis().SetTitleOffset(1.7)
#hE.Scale(1./hE.Integral())
hE.SetLineColor(1)
hE.Draw('HIST')


#h0.GetXaxis().SetTitle('ROI score')
#h0.GetYaxis().SetTitle('Unit Normalized')
#h0.GetYaxis().SetTitleOffset(1.3)
#h0.Scale(1./h0.Integral())
#h0.SetLineColor(1)
#h0.Draw('HIST')
#h0.GetXaxis().SetRangeUser(0.0,1.0)
#h0.GetYaxis().SetRangeUser(0.00001,1.0)
#
#h1.Scale(1./h1.Integral())
#h1.SetLineColor(2)
#h1.Draw('HIST SAME')
#
#h2.Scale(1./h2.Integral())
#h2.SetLineColor(3)
#h2.Draw('HIST SAME')
#h3.Scale(1./h3.Integral())
#h3.SetLineColor(4)
#h3.Draw('HIST SAME')
#legend = TLegend(0.45,0.75,0.85,0.87) 		
#legend.SetBorderSize(0)
#legend.SetTextSize(.0275)
##legend.SetNColumns(2)
#legend.SetFillColor(kWhite)
#legend.SetFillColor(kWhite)
#legend.AddEntry(h0,"Signal (MS,ctau)=(15GeV,100mm)","l")
#legend.AddEntry(h1,"TTJets","l")
#legend.AddEntry(h2,"SingleTop","l")
#legend.AddEntry(h3,"WJets","l")
#legend.Draw()
avg = hE.GetMean()
avg = round(avg,5)
final = (maxval-minval)/avg

final = round(final,5)
str2='min(<S>_pe) ='+str(minval)
str1='max(<S>_pe) ='+str(maxval)
str3='(max-min)/avg ='+str(final)
fitbox = TPaveText(.7,.3,.9,.5,"brNDC")
fitbox.SetBorderSize(1)
fitbox.SetFillColor(0)
fitbox.SetTextSize(0.025)
fitbox.AddText(str1)
fitbox.AddText(str2)
fitbox.AddText(str3)
fitbox.Draw()
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
extra.DrawTextNDC(0.3,0.91,"Work In Progress")
extra2.DrawLatexNDC(0.55,0.91,"Phase2 GeoD86")
c1.Modified()
c1.Update()
#k=raw_input('Press ENTER to exit')
c1.SaveAs('startup4mmsipm.png')
c1.SaveAs('startup4mmsipm.pdf')
k=raw_input('Press ENTER to exit')
