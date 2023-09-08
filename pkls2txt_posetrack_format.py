import numpy as np
from tqdm import tqdm
import motmetrics as mm
from utils.utils_measure import _from_dense
import trackeval as trackeval
import sys
from tqdm import tqdm
import joblib
import os
from pdb import set_trace
    



if __name__ == '__main__':
    data_gt = joblib.load('_DATA/posetrack/posetrack18_gt_data.pickle') 

    results_dir = str(sys.argv[1])
    method      = str(sys.argv[2])
    dataset     = str(sys.argv[3])

    data_all = joblib.load(results_dir + '/'+str(dataset)+'_'+str(method)+'.pkl')        
    txt_path = results_dir+'/posetrack21_txt/'
    
    #for video in tqdm(list(data_all.keys())):
    for video in tqdm(list(data_gt.keys())):
        file = open(txt_path+video+'.txt','w')

        #list_of_predictions  = []
        #for t, frame in enumerate(data_all[video].keys()):
        #    data        = data_all[video][frame]
        #    pt_ids      = data[5]
        #    for p_ in pt_ids:
        #        list_of_predictions.append(p_)
        #list_of_predictions = np.unique(list_of_predictions)        
        print("processing: "+video )    
        #for t, frame in enumerate(data_all[video].keys()):
        for t, frame in enumerate(data_gt[video].keys()):
        
            #frame
            frame_index = t+1
            
            if video == '001022_mpii_test' and frame == '000105.jpg' :
                continue
            if video == '023963_mpii_test' and frame == '000146.jpg' :
                continue
            data = data_all[video]['/home/dobbang/jeon/PoseTrack/val/'+str(video)+'/'+frame]
            #data = data_all[video][frame]
            pt_ids_      = data[5]
            pt_bbox_     = data[6]
            
            #import cv2
            #image = cv2.imread('/home/dobbang/jeon/PoseTrack/val_deblur/'+str(video)+'/'+frame) 
            
            for p_, b_ in zip(pt_ids_, pt_bbox_):
                id = p_ # id
                x1 = int(b_[0]) #x
                y1 = int(b_[1]) #y
                w = int(b_[2]) 
                h = int(b_[3]) 
                #cv2.line(image,(x1,y1),(x1+w,y1),(255,0,0),1)
                #cv2.line(image,(x1+w,y1),(x1+w,y1+h),(255,0,0),1)
                #cv2.line(image,(x1+w,y1+h),(x1,y1+h),(255,0,0),1)
                #cv2.line(image,(x1,y1+h),(x1,y1),(255,0,0),1)

                file.write(str(frame_index)+','+str(id)+','+str(x1)+','+str(y1)+','+str(w)+','+str(h)+',1,-1,-1,-1')
                file.write('\n')
                
            #cv2.imshow("image",image)
            #cv2.waitKey(0)
        
        file.close()