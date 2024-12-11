
## 1-Feature extraction:

colmap feature_extractor --image_path "D:\oneDrive\Desktop\glotest\images" --database_path "D:\oneDrive\Desktop\glotest\database.db"

## 2-Feature matching:
colmap sequential_matcher --database_path D:\oneDrive\Desktop\glotest\database.db

## 3-sparse reconstruction:
glomap mapper --database_path D:\oneDrive\Desktop\glotest\database.db --image_path D:\oneDrive\Desktop\glotest\images --output_path D:\oneDrive\Desktop\glotest\sparse

## 4- Visualize and save project and to export results as txt:
colmap gui --import_path D:\oneDrive\Desktop\glotest\sparse\0 --image_path D:\oneDrive\Desktop\glotest\images --database_path D:\oneDrive\Desktop\glotest\database.db






-To automate this with python also it uses GPU -> conda prompt   | don't use images as a folder name it causes errors 
python "D:\oneDrive\Desktop\colmap 10\run_glomap.py" --image_path     --model_type 3dgs



https://github.com/jonstephens85/glomap_windows?tab=readme-ov-file




.venv\Scripts\python.exe colmap_sparse_reconstruction.py --colmap_exe_path "colmap\COLMAP.bat" --sequence_root "example_training_data_root\1\_start_002603_end_002984_stride_1000_segment_00" --overwrite_reconstruction


