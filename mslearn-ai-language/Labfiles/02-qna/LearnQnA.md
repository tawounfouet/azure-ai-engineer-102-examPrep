


```sh
# Prediction url
https://awf-language-001.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=LearnFAQ&api-version=2021-10-01&deploymentName=production


# Sample request 
curl -X POST "https://awf-language-001.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=LearnFAQ&api-version=2021-10-01&deploymentName=production" -H "Ocp-Apim-Subscription-Key: 07130c5b41bd4db8a8e36b62769c1960" -H "Content-Type: application/json" -d "{\"top\":3,\"question\":\"YOUR_QUESTION_HERE\",\"includeUnstructuredSources\":true,\"confidenceScoreThreshold\":\"YOUR_SCORE_THRESHOLD_HERE\",\"answerSpanRequest\":{\"enable\":true,\"topAnswersWithSpan\":1,\"confidenceScoreThreshold\":\"YOUR_SCORE_THRESHOLD_HERE\"},\"filters\":{\"metadataFilter\":{\"logicalOperation\":\"YOUR_LOGICAL_OPERATION_HERE\",\"metadata\":[{\"key\":\"YOUR_ADDITIONAL_PROP_KEY_HERE\",\"value\":\"YOUR_ADDITIONAL_PROP_VALUE_HERE\"}]}}}"


curl 
    -X POST "https://awf-language-001.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=LearnFAQ&api-version=2021-10-01&deploymentName=production" 
    -H "Ocp-Apim-Subscription-Key: 07130c5b41bd4db8a8e36b62769c1960" 
    -H "Content-Type: application/json" 
    -d "{\"top\":3,\"question\":\"YOUR_QUESTION_HERE\",\"includeUnstructuredSources\":true,\"confidenceScoreThreshold\":\"YOUR_SCORE_THRESHOLD_HERE\",\"answerSpanRequest\":{\"enable\":true,\"topAnswersWithSpan\":1,\"confidenceScoreThreshold\":\"YOUR_SCORE_THRESHOLD_HERE\"},\"filters\":{\"metadataFilter\":{\"logicalOperation\":\"YOUR_LOGICAL_OPERATION_HERE\",\"metadata\":[{\"key\":\"YOUR_ADDITIONAL_PROP_KEY_HERE\",\"value\":\"YOUR_ADDITIONAL_PROP_VALUE_HERE\"}]}}}"
````