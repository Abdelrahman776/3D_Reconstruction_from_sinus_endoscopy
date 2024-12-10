must uplload to github

# video to framessss

ffmpeg -i input_video.mp4 -vf "fps=17" -q:v 2 images/%04d.jpg

# step 3 , 8

.venv\Scripts\python.exe colmap_model_converter.py --colmap_exe_path "colmap\COLMAP.bat" --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" --overwrite_output





# step 5

.venv\Scripts\python.exe dense_feature_matching.py --image_downsampling 4.0 --network_downsampling 64 --input_size 256 320 --batch_size 1 --num_workers 1 --load_intermediate_data --data_root "example_training_data_root" --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" --trained_model_path "dense_reconstruction_trained_models\descriptor\bag_1_colmap_only\checkpoint_model_epoch_100_0.7375500110313298_0.8749000144898892_0.9466000116430223.pt" --precompute_root "new precompute" --feature_length 128 --filter_growth_rate 10 --max_feature_detection 3000 --cross_check_distance 3.0 --patient_id 1 --gpu_id 0 --temporal_range 30 --test_keypoint_num 200 --residual_threshold 5.0 --octave_layers 8 --contrast_threshold 5e-5 --edge_threshold 100 --sigma 1.1 --skip_interval 5 --min_inlier_ratio 0.2 --hysterisis_factor 0.7


-----------------------------------------------------------------------------------
.venv\Scripts\python.exe dense_feature_matching.py --image_downsampling 4.0 --network_downsampling 64 --input_size 256 320 --batch_size 1 --num_workers 1  --data_root "example_training_data_root" --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" --trained_model_path "dense_reconstruction_trained_models\descriptor\bag_1_colmap_only\checkpoint_model_epoch_100_0.7375500110313298_0.8749000144898892_0.9466000116430223.pt" --precompute_root "new precompute" --feature_length 128 --filter_growth_rate 10 --max_feature_detection 3000 --cross_check_distance 3.0 --patient_id 1 --gpu_id 0 --temporal_range 30 --test_keypoint_num 200 --residual_threshold 5.0 --octave_layers 8 --contrast_threshold 5e-5 --edge_threshold 100 --sigma 1.1 --skip_interval 5 --min_inlier_ratio 0.2 --hysterisis_factor 0.7



# step 6

.venv\Scripts\python.exe colmap_database_creation.py --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" 

try to overwrite or delete database.db
# step 7

glomap mapper --database_path D:\oneDrive\Desktop\3D_Reconstruction_from_sinus_endoscopy\example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00\database.db --image_path D:\oneDrive\Desktop\3D_Reconstruction_from_sinus_endoscopy\example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00\images --output_path D:\oneDrive\Desktop\3D_Reconstruction_from_sinus_endoscopy\example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00\dense   colmaps


------------------------------------------------------------------------------------------------------
.venv\Scripts\python.exe colmap_sparse_reconstruction.py --colmap_exe_path "colmap\COLMAP.bat" --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" --overwrite_reconstruction

# step 9 not working yet

.venv\Scripts\python.exe train_depth_estimation.py --adjacent_range 5 30 --image_downsampling 4.0 --network_downsampling 64 --input_size 256 320 --batch_size 1 --num_workers 1 --slp_weight 0.05 --dcl_weight 0.5 --sfl_weight 10 --dl_weight 0.05 --lr_range 1.0e-4 1.0e-3 --inlier_percentage 0.9 --display_interval 20 --visible_interval 5 --save_interval 1 --training_patient_id 1 --num_epoch 40 --num_iter 1000 --display_architecture --data_root "example_training_data_root" --log_root "new precompute\logs" --precompute_root "new precompute" --descriptor_model_path "dense_reconstruction_trained_models\descriptor\bag_1_colmap_only\checkpoint_model_epoch_100_0.7375500110313298_0.8749000144898892_0.9466000116430223.pt" --load_trained_model --trained_model_path "dense_reconstruction_trained_models\depth_estimation\checkpoint_model_epoch_114_validation_4.52560411356001_5.486630147792803*-1.4580580111325379_0.4970320685285854.pt"

---

.venv\Scripts\python.exe train_depth_estimation.py --adjacent_range 5 30 --image_downsampling 4.0 --network_downsampling 64 --input_size 256 320 --batch_size 1 --num_workers 1 --slp_weight 0.05 --dcl_weight 0.5 --sfl_weight 10 --dl_weight 0.05 --lr_range 1.0e-4 1.0e-3 --inlier_percentage 0.9 --display_interval 20 --visible_interval 5 --save_interval 1 --training_patient_id 1 --num_epoch 40 --num_iter 1000 --architecture_summary --display_architecture --load_intermediate_data --data_root "example_training_data_root" --log_root "new precompute\logs" --precompute_root "new precompute" --descriptor_model_path "dense_reconstruction_trained_models\descriptor\bag_1_colmap_only\checkpoint_model_epoch_100_0.7375500110313298_0.8749000144898892_0.9466000116430223.pt" --load_trained_model --trained_model_path "dense_reconstruction_trained_models\depth_estimation\checkpoint_model_epoch_114_validation_4.52560411356001_5.486630147792803*-1.4580580111325379_0.4970320685285854.pt"

---

/path/to/python /path/to/train_depth_estimation.py --adjacent_range 5 30 --image_downsampling 4.0 --network_downsampling 64 --input_size 256 320 --batch_size 4 --num_workers 4 --slp_weight 1.0 --dcl_weight 0.5 --sfl_weight 2.0 --dl_weight 0.05 --lr_range 1.0e-4 1.0e-3 --inlier_percentage 0.9 --display_interval 20 --visible_interval 5 --save_interval 1 --training_patient_id 1 --num_epoch 40 --num_iter 1000 --display_architecture --load_intermediate_data --data_root "/path/to/training/data/root" --log_root "/path/to/log/root" --precompute_root "/path/to/precompute/root" --descriptor_model_path "/path/to/trained/descriptor/model"

# step 10


.venv\Scripts\python.exe fusion_data_generation.py --image_downsampling 4.0 --network_downsampling 64 --input_size 256 320 --batch_size 1 --num_workers 1 --visible_interval 5 --inlier_percentage 0.9  --trained_model_path "dense_reconstruction_trained_models\depth_estimation\checkpoint_model_epoch_114_validation_4.52560411356001_5.486630147792803_-1.4580580111325379_0.4970320685285854.pt" --data_root "example_training_data_root" --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" --patient_id 1 --precompute_root "new precompute"


# step 11


.venv\Scripts\python.exe surface_reconstruction.py --data_root "example_training_data_root" --trunc_margin_multiplier 20.0 --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" --patient_id 1 --max_voxel_count 27e6
------------------------------------------------------------------------------------------------------------------------

.venv\Scripts\python.exe surface_reconstruction.py --data_root "example_training_data_root" --trunc_margin_multiplier 10.0 --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" --patient_id 1 --max_voxel_count 64e6


.venv\Scripts\python.exe surface_reconstruction.py --data_root "example_training_data_root" --trunc_margin_multiplier 10.0 --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" --patient_id 1 --max_voxel_count 27e6


.venv\Scripts\python.exe surface_reconstruction.py --data_root "example_training_data_root" --trunc_margin_multiplier 20.0 --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" --patient_id 1 --max_voxel_count 64e6



must uplload to github
