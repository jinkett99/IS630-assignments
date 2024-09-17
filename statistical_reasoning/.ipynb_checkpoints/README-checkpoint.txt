Solution to explore – Re-train new ML model optimized on SOE data
	1. Extract SOE data – 2023, preferably 2022 as well (to separate years)
	2. Train RF classifier & XGBoostmodel on datasets
	3. Obtain evaluation metrics.
    4. Run new model on 2022 & 2023 base datasets (ie2022, ie2023)
    5. Review class distributions of 'B' & 'C'.
    
Imputations of firms with websites using SOE data. 

--- Storyline & Steps Taken ---
Title: Investigating Distribution of Revenue-Generating Websites (IE2023)
Background information: 
- The IE team recently reviewed IE2023 results & found that there were some issues with the distribution of revenue-generating websites. I.e. Almost one in every two websites are revenue generating in 2023. 
- This review aims to dive deep into the ML and analytics lifecycle to investigate the nuances in trends observed (i.e. High proportions of firms with revenue-generating websites)

Overall review process: 
1. Look into ML RF classifier - Conclusion was that it was unlikely that the model 'overestimated' the proportion of class "C" labels as the FN and FP rates were similar. *Show confusion matrix & classification report. 
2. Eyeball/Review of misclassified "revenue-generating" websites (i.e. firms predicted as "C" but in actual fact, was "B" - non-revenue generating) - Conclusion was that there were these websites present.
3. Train a new RF classifier on latest (2022) SOE dataset (ground truth) & re-run inference/predictions on 2022 dataset. *Reflect charts as outcomes. 
4. Re-run imputation steps (for internal info.)
5. Present new findings*