# Reconstructing Sinus Anatomy from Endoscopic Videos 
This is a part of our graduation project Virtual Reality Training Platform for Neurosurgery

![alt text](gifss/image-2.png)

![](gifss/fused_mesh.gif) 

*Left to right: original video, 3D reconstruction fly-through, depth rendering, monocular depth estimate, monocular depth uncertainty estimate*

This codebase is an re-implementation of a patient-specific, learning-based 3D reconstruction method for sinus surface anatomy using only endoscopic videos, the method described in the paper:

[***Reconstructing Sinus Anatomy from Endoscopic Video -- Towards a Radiation-free Approach for Quantitative Longitudinal Assessment***](https://link.springer.com/chapter/10.1007/978-3-030-59716-0_1)

## The paper pipeline:
![alt text](gifss/image.png)



cite [this paper](https://link.springer.com/chapter/10.1007/978-3-030-59716-0_1) if the code is used in your own work.
Xingtong Liu, Maia Stiber, Jindan Huang, Masaru Ishii, Gregory D. Hager, Russell H. Taylor, Mathias Unberath



Please contact [**Xingtong Liu**](http://www.cs.jhu.edu/~xingtongl/) (xingtongliu@jhu.edu) or [**Mathias Unberath**](https://www.cs.jhu.edu/faculty/mathias-unberath/) (unberath@jhu.edu) if you have any questions.




## Instructions
1. Install all necessary python packages: 
```
torch, torchvision, opencv-python (<= 3.4.2.16), opencv-contrib-python (<= 3.4.2.16), numpy, tqdm, pathlib, torchsummary, tensorboardX, albumentations, argparse, pickle, plyfile, pyyaml, datetime, random, shutil, matplotlib, tensorflow, autolab_core, autolab_perception, meshrender, h5py, trimesh, scikit-image, sqlite3
```
or instead we will provide a [download link]() to our python virtual environment (.venv) where all the packages are downloaded.
you have to put the environment folder in the repo folder.
 
2. Make a folder named images where you have your Color image frames with the format ```{:08d}.jpg``` which are extracted from the endoscopy video. 

2. Generate SfM results from videos using Structure from Motion (SfM), e.g. [COLMAP](https://colmap.github.io/).
we recommend following this [tutorial](https://www.youtube.com/watch?v=QIxXuilEEVw) to download COLMAP and new add-on called GLOMAP that generates sfm results significantly faster.you can use ```colmap steps.md``` where the commands from the tutorial are written.
3. make a folder called ```colmap\0```where  your  files cameras.bin, images.bin and points3D.bin and their txt equivalents must be included. These files include the intrinsic camera parameters, extrinsic camera parameters and sparse points, respectively.
3. Now you have two folders ```images``` with your images in it and ```comap``` folder with your sfm results. 
![alt text](gifss/image-1.jpg)
![alt text](gifss/image-5.png)

7. put these two folders in a folder structure similar to the example in the next step. It will be like this```example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00\images```
and 
```example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00\colmap```
8. You need to make ```undistorted_mask.bmp``` which is a binary mask used to mask out blank regions of the endoscopic video frames. if you don't have one for your videos use a take frame from your video and convert it to a black and white (binary) mask using photo-editing software like photoshop or photopea.put the mask on the same folder with ```colmap``` and ```images``` and inside ```colmap\0```.
<!--it looks like this : ![alt text](gifss/undistorted_mask.bmp)-->

9. Use the same folder names to be able to directly use our commands from ```commands.md``` or you can change the commands with respect to you folders names. we also provide each command template after each step of the pipeline.

10. Convert SfM results to the format similar to [this storage](https://livejohnshopkins-my.sharepoint.com/:u:/g/personal/xliu89_jh_edu/ER5ght84vKdHmdYrBpS7HCMBQn9Kl152kVTPB5R10ofKDw?e=fY85o6). 

It will include:

 - ```camer_intrinsics_per_view``` stores ```fx, fy, cx, cy``` element of the estimated camera intrinsics. In this example, since all images are from the same video sequence, we assume the intrinsics are the same for all frames. 

- ```motion.yaml``` stores the estimated poses of the camera coordinate system w.r.t. the world coordinate system. 

- ```selected_indexes``` stores all frame indexes of the video sequence.

 - ```structure.ply``` stores the estimated sparse 3D reconstruction from SfM. 

 - ```undistorted_mask.bmp``` is a binary mask used to mask out blank regions of the video frames. 

- ```view_indexes_per_point``` stores the indexes of the frames that each point in the sparse reconstruction gets triangulated with. The views per point are separated by -1 and the order of the points is the same as that in ```structure.ply```. We smooth out the point visibility information in the script to make the global scale recovery more stable and obtain more sparse points per frame for training. 
The point visibility smoothness is controled by parameter ```visibility_overlap```. 

 - ```visible_view_indexes``` stores the original frame indexes of the registered views where valid camera poses are successfully estimated by SfM.

  To convert SfM results from COLMAP to the required format, one example for using ```colmap_model_converter.py``` is:
```
/path/to/python /path/to/colmap_model_converter.py --colmap_exe_path "/path/to/COLMAP.bat" --sequence_root "/path/to/video/sequence"
```
11. To skip training the models download the **Pre-trained models**

The pre-trained weights for dense descriptor network and depth estimation network are provided [here](https://drive.google.com/file/d/1RwmxpI7kuZ7teB14EQY3u06CAV7-KsX0/view?usp=sharing).

12. (optional) Train a feature descriptor model for pair-wise feature matching in SfM. One example for using ```train_descriptor.py``` is:
```
/path/to/python /path/to/train_descriptor.py --adjacent_range 1 50 --image_downsampling 4.0 --network_downsampling 64 --input_size 256 320 --batch_size 4 --num_workers 4 --lr_range 1.0e-4 1.0e-3 --inlier_percentage 0.9 --display_interval 50 --validation_interval 2 --training_patient_id 1 --load_intermediate_data --num_epoch 60 --num_iter 1000 --heatmap_sigma 5.0 --visibility_overlap 20 --display_architecture --data_root "/path/to/training/data/root" --sampling_size 10 --log_root "/path/to/log/root" --feature_length 128 --filter_growth_rate 10 --matching_scale 20.0 --matching_threshold 0.9 --rr_weight 1.0 --cross_check_distance 3.0 --precompute_root "/path/to/precompute/root"
```
```--load_trained_model --trained_model_path "/path/to/trained/model"``` can be added to continue previous training.

13. Run ```dense_feature_matching.ply``` with the trained descriptor model to generate pair-wise feature matches for SfM running. One example is:
```
/path/to/python /path/to/dense_feature_matching.py --image_downsampling 4.0 --network_downsampling 64 --input_size 256 320 --batch_size 1 --num_workers 1  --load_intermediate_data --data_root "/path/to/data/root" --sequence_root "/path/to/sequence/data" --trained_model_path "/path/to/trained/descriptor/model" --precompute_root "/path/to/precompute/root" --feature_length 128 --filter_growth_rate 10 --max_feature_detection 3000 --cross_check_distance 3.0 --patient_id 1 --gpu_id 0 --temporal_range 30 --test_keypoint_num 200 --residual_threshold 5.0 --octave_layers 8 --contrast_threshold 5e-5 --edge_threshold 100 --sigma 1.1 --skip_interval 5 --min_inlier_ratio 0.2 --hysterisis_factor 0.7     
```

14. Run ```colmap_database_creation.py``` to convert the generated feature matches in HDF5 format to SQLite format, named ```database.db```, that is compatible with COLMAP. One example is:
```
/path/to/python /path/to/colmap_database_creation.py --sequence_root "/path/to/video/sequence"
```

15. Run ```colmap_sparse_reconstruction.py``` to run ```mapper``` in COLMAP for bundle adjustment to generate sparse reconstruction and camera trajectory. One usage example is:
```
/path/to/python /path/to/colmap_sparse_reconstruction.py --colmap_exe_path "/path/to/COLMAP.bat" --sequence_root "/path/to/video/sequence"
```
or Run Glomap  mapper  for faster results:
```
glomap mapper --database_path path\database.db --image_path path\images --output_path path\colmap\0 
```

16.  Run ```colmap_model_converter.py``` again to convert the SfM result from COLMAP with the trained feature descriptor to the required format for training a depth estimation model. See step 3 for one example.

17. (optional) Train a depth estimation model with the data generated in step 8. The previous trained descriptor model can be used to calculate an optional appearance consistency loss. One example is:
```
/path/to/python /path/to/train_depth_estimation.py --adjacent_range 5 30 --image_downsampling 4.0 --network_downsampling 64 --input_size 256 320 --batch_size 4 --num_workers 4 --slp_weight 1.0 --dcl_weight 0.5 --sfl_weight 2.0 --dl_weight 0.05 --lr_range 1.0e-4 1.0e-3 --inlier_percentage 0.9 --display_interval 20 --visible_interval 5 --save_interval 1 --training_patient_id 1 --num_epoch 40 --num_iter 1000 --display_architecture --load_intermediate_data --data_root "/path/to/training/data/root" --log_root "/path/to/log/root" --precompute_root "/path/to/precompute/root" --descriptor_model_path "/path/to/trained/descriptor/model"
```
```--load_trained_model --trained_model_path "/path/to/trained/model"``` can be added to continue previous training.

18. Run ```fusion_data_generation.py``` to generate depth estimates for model fusion later. One example is:
```
/path/to/python /path/to/fusion_data_generation.py --image_downsampling 4.0 --network_downsampling 64 --input_size 256 320 --batch_size 1 --num_workers 1 --visible_interval 5 --inlier_percentage 0.9 --load_intermediate_data --trained_model_path "/path/to/trained/model" --data_root "/path/to/data/root" --sequence_root "/path/to/sequence/root" --patient_id 1 --precompute_root "/path/to/precompute/root"
```
![alt text](gifss/image-3.png)

19. Run ```surface_reconstruction.py``` to generate the textured watertight surface reconstruction. A fly-through video will also be generated for sanity check. One example is:
```
/path/to/python /path/to/surface_reconstruction.py --data_root "/path/to/data/root" --visualize_fused_model --trunc_margin_multiplier 10.0 --sequence_root "/path/to/sequence/root" --patient_id 1 --max_voxel_count 64e6
```


![alt text](gifss/image-4.png)



















## Related Projects

- [SAGE: SLAM with Appearance and Geometry Prior for Endoscopy (ICRA 2022)](https://github.com/lppllppl920/SAGE-SLAM)

- [Neighborhood Normalization for Robust Geometric Feature Learning (CVPR 2021)](https://github.com/lppllppl920/NeighborhoodNormalization-Pytorch)

- [Extremely Dense Point Correspondences using a Learned Feature Descriptor (CVPR 2020)](https://github.com/lppllppl920/DenseDescriptorLearning-Pytorch)

- [Dense Depth Estimation in Monocular Endoscopy with Self-supervised Learning Methods (TMI)](https://github.com/lppllppl920/EndoscopyDepthEstimation-Pytorch)
