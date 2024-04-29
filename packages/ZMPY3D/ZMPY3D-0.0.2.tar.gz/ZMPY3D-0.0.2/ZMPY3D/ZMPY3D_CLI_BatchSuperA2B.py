# MIT License
#
# Copyright (c) 2024 Jhih-Siang Lai
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import numpy as np
import pickle
import argparse
import os
import sys

import ZMPY3D as z

def ZMPY3D_CLI_BatchSuperA2B(PDBFileNameA, PDBFileNameB):
    def ZMCal(PDBFileName,GridWidth,BinomialCache, CLMCache, CLMCache3D, GCache_complex, GCache_complex_index, GCache_pqr_linear, MaxOrder, Param, ResidueBox, RotationIndex):

        [XYZ,AA_NameList]=z.get_pdb_xyz_ca(PDBFileName);

        [Voxel3D,Corner]=z.fill_voxel_by_weight_density(XYZ,AA_NameList,Param['residue_weight_map'],GridWidth,ResidueBox[GridWidth]);
        Dimension_BBox_scaled=Voxel3D.shape;

        XYZ_SampleStruct = {
            'X_sample': np.arange(Dimension_BBox_scaled[0] + 1),
            'Y_sample': np.arange(Dimension_BBox_scaled[1] + 1),
            'Z_sample': np.arange(Dimension_BBox_scaled[2] + 1)
        }
        
        [VolumeMass,Center,_]=z.calculate_bbox_moment(Voxel3D,1,XYZ_SampleStruct);
        [AverageVoxelDist2Center,MaxVoxelDist2Center]=z.calculate_molecular_radius(Voxel3D,Center,VolumeMass,Param['default_radius_multiplier'])

        ##################################################################################
        # You may add any preprocessing on the voxel before applying the Zernike moment. #
        ##################################################################################

        Center_scaled=Center*GridWidth+Corner
        
        SphereXYZ_SampleStruct=z.get_bbox_moment_xyz_sample(Center,AverageVoxelDist2Center,Dimension_BBox_scaled)
        _,_,SphereBBoxMoment=z.calculate_bbox_moment(Voxel3D,MaxOrder,SphereXYZ_SampleStruct)
        
        [ZMoment_scaled, ZMoment_raw]=z.calculate_bbox_moment_2_zm(MaxOrder, GCache_complex, GCache_pqr_linear, GCache_complex_index, CLMCache3D, SphereBBoxMoment)

        ABList_2=z.calculate_ab_rotation_all(ZMoment_raw, 2)
        ABList_3=z.calculate_ab_rotation_all(ZMoment_raw, 3)
        ABList_4=z.calculate_ab_rotation_all(ZMoment_raw, 4)
        ABList_5=z.calculate_ab_rotation_all(ZMoment_raw, 5)
        ABList_6=z.calculate_ab_rotation_all(ZMoment_raw, 6)
        
        ABList_all=np.vstack(ABList_2+ABList_3+ABList_4+ABList_5+ABList_6) 
    
        ZMList_all=z.calculate_zm_by_ab_rotation(ZMoment_raw, BinomialCache, ABList_all, MaxOrder, CLMCache,s_id,n,l,m,mu,k,IsNLM_Value)
        ZMList_all=np.stack(ZMList_all,axis=3)

        ZMList_all=np.transpose(ZMList_all,(2,1,0,3)) 
        ZMList_all=ZMList_all[~np.isnan(ZMList_all)]
        # Based on ABList_all, it is known in advance that Order 6 will definitely have 96 pairs of AB, which means 96 vectors.
        ZMList_all=np.reshape(ZMList_all,(np.int64(ZMList_all.size/96),96))
    
        return XYZ, Center_scaled, ABList_all,ZMList_all,AA_NameList
    
    Param=z.get_global_parameter();
    
    MaxOrder=6
    

    BinomialCacheFilePath = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache_data'), 'BinomialCache.pkl')
    with open(BinomialCacheFilePath, 'rb') as file: # Used at the entry point, it requires __file__ to identify the package location
    # with open('./cache_data/BinomialCache.pkl', 'rb') as file: # Can be used in ipynb, but not at the entry point. 
        BinomialCachePKL = pickle.load(file)

    LogCacheFilePath=os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache_data'), 'LogG_CLMCache_MaxOrder{:02d}.pkl'.format(MaxOrder))
    with open(LogCacheFilePath, 'rb') as file: # Used at the entry point, it requires __file__ to identify the package location
    # with open('./cache_data/LogG_CLMCache_MaxOrder{:02d}.pkl'.format(MaxOrder), 'rb') as file: # Can be used in ipynb, but not at the entry point. 
        CachePKL = pickle.load(file)  

    # Extract all cached variables from pickle. These will be converted into a tensor/cupy objects for ZMPY3D_CP and ZMPY3D_TF.
    BinomialCache=BinomialCachePKL['BinomialCache']
    
    # GCache, CLMCache, and all RotationIndex
    GCache_pqr_linear=CachePKL['GCache_pqr_linear']
    GCache_complex=CachePKL['GCache_complex']
    GCache_complex_index=CachePKL['GCache_complex_index']
    CLMCache3D=CachePKL['CLMCache3D']
    CLMCache=CachePKL['CLMCache']
    RotationIndex=CachePKL['RotationIndex']
    
    # RotationIndex is a structure, must be [0,0] to accurately obtain the s_id ... etc, within RotationIndex.
    s_id=np.squeeze(RotationIndex['s_id'][0,0])-1
    n   =np.squeeze(RotationIndex['n'][0,0])
    l   =np.squeeze(RotationIndex['l'][0,0])
    m   =np.squeeze(RotationIndex['m'][0,0])
    mu  =np.squeeze(RotationIndex['mu'][0,0])
    k   =np.squeeze(RotationIndex['k'][0,0])
    IsNLM_Value=np.squeeze(RotationIndex['IsNLM_Value'][0,0])-1   

    MaxN=MaxOrder+1
    
    ResidueBox=z.get_residue_gaussian_density_cache(Param)

    GridWidth= 1.00; 

    TargetRotM = []
    
    for index in range(len(PDBFileNameA)):
        XYZ_A, Center_scaled_A,ABList_A,ZMList_A,AA_NameList_A =ZMCal(PDBFileNameA[index],1.00,BinomialCache, CLMCache, CLMCache3D, GCache_complex, GCache_complex_index, GCache_pqr_linear, MaxOrder, Param, ResidueBox, RotationIndex)
        XYZ_B, Center_scaled_B,ABList_B,ZMList_B,AA_NameList_B =ZMCal(PDBFileNameB[index],1.00,BinomialCache, CLMCache, CLMCache3D, GCache_complex, GCache_complex_index, GCache_pqr_linear, MaxOrder, Param, ResidueBox, RotationIndex)

        M = np.abs(ZMList_A.conj().T @ ZMList_B) # square matrix A^T*B 
        MaxValueIndex = np.where(M == np.max(M)) # MaxValueIndex is a tuple that contains an nd array.
    
        i, j = MaxValueIndex[0][0], MaxValueIndex[1][0]
        
        RotM_A=z.get_transform_matrix_from_ab_list(ABList_A[i,0],ABList_A[i,1],Center_scaled_A)
        RotM_B=z.get_transform_matrix_from_ab_list(ABList_B[j,0],ABList_B[j,1],Center_scaled_B)

        TargetRotM.append(np.linalg.solve(RotM_B, RotM_A))

    return TargetRotM



import sys
import argparse
import os

def main():
    if len(sys.argv) != 2:
        print('Usage: ZMPY3D_CLI_BatchSuperA2B PDBFileList.txt')
        print('       This function takes a list of paired PDB structure file paths to generate transformation matrices.')
        print("Error: You must provide exactly one input file.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Process input file that contains paths to .pdb or .txt files.')
    parser.add_argument('input_file', type=str, help='The input file that contains paths to .pdb or .txt files.')

    args = parser.parse_args()

    input_file = args.input_file
    if not input_file.endswith('.txt'):
        parser.error("File must end with .txt")
    
    if not os.path.isfile(input_file):
        parser.error("File does not exist")

    with open(input_file, 'r') as file:
        lines = file.readlines()

    file_list_1 = []
    file_list_2 = []
    for line in lines:

        files = line.strip().split()
        if len(files) != 2:
            print(f"Error: Each line must contain exactly two file paths, but got {len(files)}.")
            sys.exit(1)
        file1, file2 = files

        
        for file in [file1, file2]:
            if not (file.endswith('.pdb') or file.endswith('.txt')):
                print(f"Error: File {file} must end with .pdb or .txt.")
                sys.exit(1)
            if not os.path.isfile(file):
                print(f"Error: File {file} does not exist.")
                sys.exit(1)
        file_list_1.append(file1)
        file_list_2.append(file2)

    TargetRotM=ZMPY3D_CLI_BatchSuperA2B(file_list_1, file_list_2)

    for M in TargetRotM:
        print(M)

if __name__ == '__main__':
    main()