import sys
import numpy as np
from ROOT import *

def makeHist(x,y,label):
        gROOT.SetBatch(kTRUE)
        c1 = TCanvas ("c1")
        gPad.SetLeftMargin(0.13)
        gPad.SetBottomMargin(0.12)
        gPad.SetTickx()
        gPad.SetTicky()
        gPad.SetLogz()
        gStyle.SetOptStat(0)
        gStyle.SetLineWidth(3)
        gStyle.SetHistLineWidth(3)
        h0  = TH2F( 'test', 'ROI Score vs. ' + label, 50, 0, np.max(x), 50, 0, 1)

        for i in np.arange(0, y.size):
                h0.Fill(x[i],y[i])
                #h0.Fill(x[i],np.log10(1-y[i]))
        h0.Draw('COLZ')
        h0.GetXaxis().SetTitle(label)
        h0.GetYaxis().SetTitle('ROI Score')
        h0.GetYaxis().SetTitleOffset(1.3)

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
        #title.DrawTextNDC(0.2,0.91,"CMS")
        #extra.DrawTextNDC(0.3,0.91,"Preliminary")
        #extra2.DrawLatexNDC(0.55,0.91,"Run2")
        c1.Modified()
        c1.Update()
        c1.SaveAs(label+'.pdf')


signal_dataset_name = sys.argv[1]
train = np.load('ggH_HToSSTo4Tau_MH-125_MS-7_ctauS-10.npz')
outputname = np.load(signal_dataset_name+'_output.npz')

output = outputname['outputs_data']

vertex_train = train['vertex_data']
annulus_train = train['annulus_data']
event_train = train['event_data']
#markers_train = train['markers_data']
auxiliary_train = train['auxiliary_data']

#vertex_val = validation['vertex_val']
#annulus_val = validation['annulus_val']
#event_val = validation['event_val']
#markers_val= validation['markers_val']
#auxiliary_val = validation['auxiliary_val']

#vertex_test = test['vertex_test']
#annulus_test = test['annulus_test']
#event_test = test['event_test']
#markers_test = test['markers_test']
#auxiliary_test = test['auxiliary_test']


vertex_labels = ['trackCluster_vx','trackCluster_vy', 'trackCluster_vz',
                     'trackCluster_vertexCovariance(0, 0)', 'trackCluster_vertexCovariance(0, 1)', 'trackCluster_vertexCovariance(0, 2)',
                     'trackCluster_vertexCovariance(1, 0)', 'trackCluster_vertexCovariance(1, 1)',
                     'trackCluster_vertexCovariance(1, 2)',
                     'roiTracks[0]_signedPt', 'roiTracks[0]_eta', 'roiTracks[0]_phi', 'roiTracks[0]_dxy', 'roiTracks[0]_dz',
                     'roiTracks[0]_normalizedChi2', 'roiTracks[0]_highPurity',
                     'roiTracks[1]_signedPt', 'roiTracks[1]_eta', 'roiTracks[1]_phi', 'roiTracks[1]_dxy', 'roiTracks[1]_dz',
                     'roiTracks[1]_normalizedChi2', 'roiTracks[1]_highPurity']

annulus_labels = ['track_signedPt', 'track_eta', 'track_phi', 'track_dxy', 'track_dz',
                     'track_normalizedChi2', 'track_highPurity', 'track_deltaRToROI']		

auxiliary_labels = ['regionOfInterest_vx', 'regionOfInterest_vy', 'regionOfInterest_vz', 'regionOfInterest_nConstituents']


#vertex_labels_plots = vertex_labels[9:16]
y = output
for i in np.arange(9,16):
	x = np.abs(vertex_train[:,0,i])
	#x = np.abs(vertex_train[:,0][:,i])
	label = vertex_labels[i]
	print('Making histogram for: ' + label)
	makeHist(x,y,label)

for i in np.arange(0,8):
        x = np.abs(annulus_train[:,0,i])
        #x = np.abs(annulus_train[:,0][:,i])
        label = annulus_labels[i]
        print('Making histogram for: ' + label)
        makeHist(x,y,label)

for i in np.arange(0,4):
	x = np.abs(auxiliary_train[:,i])
	label = auxiliary_labels[i]
	print('Making histogram for: ' + label)
        makeHist(x,y,label)
