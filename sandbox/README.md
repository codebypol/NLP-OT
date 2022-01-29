List of every transformations we thought about. They can be divided into 3 categories : 

* Cosine transformations : simple transformations of the cosine similarity.

    * *cosine_distance*
    * *cosine_minmax*
    * *cosine_maxabs*
    * *cosine_square*
    * *cosine_norm*
    * *cosine_arccos*
    * *cosine_normalized*
    * *cosine_robust*
    * *cosine_QT*
    * *cosine_PT*
    * *cosine_inverse*
    * *cosine_sqrt*
    * *cosine_alpha*
    * *cosine_inverse_exp*
    * *cosine_robust_inverse*
    * *cosine_square_inverse(*
    * *cosine_upped*
    * *cosine_square_smoothed*
    * *cosine_exp*
    * *cosine_SPE*
    * *cosine_transform*

* Outlier detection : non-linear methods expanding the tails of the distributions without touching at the core of the distribution.

    * *outliers*
    * *last_alpha*
    * *f_outliers*
    * *disc_square*
    * *disc_exp*

Those transformations can be compared with the method *compare()* taking two arguments : the list of the transformations to compare and the number of sentences to compare on. By default, the number of sentences is set to 5 as it is not necessary to use more.
    
