import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from skimage.feature import *
from sklearn.metrics import *
import glob,os,cv2
import os
import pandas as pd
import numpy as np
import cv2
from scipy.stats import skew, kurtosis, entropy
def extract(image_path,classname,technique_list):
    image_files = os.listdir(image_path)
    images_g=[]
    for filename in image_files:
        # Get the full path of the image file
        image_dir = os.path.join(image_path, filename)
        img=cv2.imread(image_dir,0)
        images_g.append(img)
    images_g=np.array(images_g)
    mean_list = []
    std_dev_list = []
    median_list = []
    min_value_list = []
    max_value_list = []
    variance_list = []
    range_list = []
    percentile_25_list = []
    percentile_75_list = []
    mode_list = []
    iqr_list = []
    cv_list = []
    mad_list = []
    rms_list = []
    energy_list = []
    contrast_list = []
    correlation_list = []
    homogeneity_list = []
    skewness_list = []
    kurtosis_list = []
    entropy_list = []

# Loop through each image
    for image_gray in images_g:
        mean_value = np.mean(image_gray)
        std_dev_value = np.std(image_gray)
        median_value = np.median(image_gray)
        min_value = np.min(image_gray)
        max_value = np.max(image_gray)
        variance_value = np.var(image_gray)
        range_value = np.ptp(image_gray)
        percentile_25_value = np.percentile(image_gray, 25)
        percentile_75_value = np.percentile(image_gray, 75)
        mode_value = np.argmax(np.bincount(image_gray.flatten()))
        iqr_value = percentile_75_value - percentile_25_value
        cv_value = std_dev_value / mean_value if mean_value != 0 else 0
        mad_value = np.mean(np.abs(image_gray - mean_value))
        rms_value = np.sqrt(np.mean(np.square(image_gray)))
        energy_value = np.sum(np.square(image_gray))
        contrast_value = np.var(image_gray)
        correlation_value = np.mean(np.corrcoef(image_gray))
        homogeneity_value = np.mean((1 / (1 + (image_gray - np.mean(image_gray))**2)))
        skewness_value = skew(image_gray.flatten())
        kurtosis_value = kurtosis(image_gray.flatten())
        entropy_value = entropy(np.histogram(image_gray.flatten(), bins=256)[0])
    
    # Append statistical features to the lists
        mean_list.append(mean_value)
        std_dev_list.append(std_dev_value)
        median_list.append(median_value)
        min_value_list.append(min_value)
        max_value_list.append(max_value)
        variance_list.append(variance_value)
        range_list.append(range_value)
        percentile_25_list.append(percentile_25_value)
        percentile_75_list.append(percentile_75_value)
        mode_list.append(mode_value)
        iqr_list.append(iqr_value)
        cv_list.append(cv_value)
        mad_list.append(mad_value)
        rms_list.append(rms_value)
        energy_list.append(energy_value)
        contrast_list.append(contrast_value)
        correlation_list.append(correlation_value)
        homogeneity_list.append(homogeneity_value)
        skewness_list.append(skewness_value)
        kurtosis_list.append(kurtosis_value)
        entropy_list.append(entropy_value)

# Create a dataframe to store the statistical features
        data = {
            'Mean': mean_list,
            'Std Dev': std_dev_list,
            'Median': median_list,
            'Min': min_value_list,
            'Max': max_value_list,
            'Variance': variance_list,
            'Range': range_list,
            'Percentile 25': percentile_25_list,
            'Percentile 75': percentile_75_list,
            'Mode': mode_list,
            'IQR': iqr_list,
            'Coefficient of Variation': cv_list,
            'Mean Absolute Deviation': mad_list,
            'Root Mean Square': rms_list,
            'Energy': energy_list,
            'Contrast': contrast_list,
            'Correlation': correlation_list,
            'Homogeneity': homogeneity_list,
            'Skewness': skewness_list,
            'Kurtosis': kurtosis_list,
            'Entropy': entropy_list
        }
    data=pd.DataFrame(data)
    for i in technique_list:
        if i=='GLCM' or i=='glcm':
            contrast_list = []
            dissimilarity_list = []
            homogeneity_list = []
            energy_list = []
            correlation_list = []

            # Loop through each image file
            for filename in images_g:
                distances = [1]  # distance between pixels
                angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # angles for texture features
                glcm = graycomatrix(filename, distances=distances, angles=angles, symmetric=True, normed=True)

                # Compute GLCM properties
                contrast = graycoprops(glcm, 'contrast').mean()
                dissimilarity = graycoprops(glcm, 'dissimilarity').mean()
                homogeneity = graycoprops(glcm, 'homogeneity').mean()
                energy = graycoprops(glcm, 'energy').mean()
                correlation = graycoprops(glcm, 'correlation').mean()

                # Append GLCM properties to the lists
                contrast_list.append(contrast)
                dissimilarity_list.append(dissimilarity)
                homogeneity_list.append(homogeneity)
                energy_list.append(energy)
                correlation_list.append(correlation)
            features=pd.DataFrame([contrast_list,dissimilarity_list,homogeneity_list,energy_list,correlation_list])
            features=features.T
            data=pd.concat([data,features],axis=1)
        elif i=='LBP' or i=='lbp':
            radius = 1
            n_points = 8 * radius
            lbp_hist_list=[]
            for filename in images_g:
                lbp = local_binary_pattern(filename, n_points, radius, method='uniform')
                lbp_hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, n_points + 3), range=(0, n_points + 2), density=True)
                lbp_hist_list.append(lbp_hist)
            lbp_hist_array = np.array(lbp_hist_list)
            d2=pd.DataFrame(lbp_hist_array)
            data=pd.concat([data,d2],axis=1)
        elif i=='brief' or i=='BRIEF':
            brief_descriptors_list = []

            # Create a BRIEF object
            brief = cv2.BRISK_create()

            # Loop through each image file
            for filename in images_g:
                keypoints, descriptors = brief.detectAndCompute(filename, None)

                # Append descriptors to the list
                if descriptors is not None:
                    brief_descriptors_list.extend(descriptors)

            # Convert the list of descriptors to a 2D array
            brief_descriptors_array = np.array(brief_descriptors_list)

            # Create a dataframe to store BRIEF descriptors
            brief_df = pd.DataFrame(brief_descriptors_array)
            data=pd.concat([data,brief_df],axis=1)     
    if classname is not None:
        data['labels']=str(classname)
    return data