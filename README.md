# ACTracker (  Multi-person Tracking Method considering Appearance Changes )

ACTracker is the series of Multi-person tracking models which outputs 2d bounding boxes and Track ID from 2d monocular videos

1. Main branch has vlaluation codes for PoseTrack18 and PoseTrack21 dataset each and visualzing code of tracking results.
   
2. PHALP-model-base branch is about the tracking model that implements 2 step tracking algorithm considering appearance changes(ByteTrack: https://github.com/ifzhang/ByteTrack). 
  
3. H4D-model-base branch is abouit the tracking model that extends PHALP-model-base tracker with new pose reconstruction model(HMR2.0) and deblur model(DeblurGAN_v2) 
