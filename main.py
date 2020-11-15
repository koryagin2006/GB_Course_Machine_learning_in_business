import shap

explainer = shap.Explainer(model, X)
shap_values = explainer(X)
shap_values