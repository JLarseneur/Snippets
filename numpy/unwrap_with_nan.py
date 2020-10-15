df_hpc_resampled.loc[~np.isnan(df_hpc_resampled["orientation"]), ["orientation"]] =\
np.unwrap(df_hpc_resampled.loc[~np.isnan(df_hpc_resampled["orientation"]), ["orientation"]], axis=0)
