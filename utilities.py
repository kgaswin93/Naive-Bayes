import stringManipulation as strman

def probEvents(events):
    probabilites = dict()
    total_events = len(events)
    for i in range(0,len(events)):
        if probabilites.get(events[i]):
            probabilites[events[i]] += 1
        else:
            probabilites[events[i]] = 1
    for key in probabilites.keys():
        probabilites[key] /= total_events
    return probabilites

def getLivelihoodTable(data_instances,class_labels,prior):
    cond_prob = dict()
    total_data_instances = len(data_instances)
    for i in range(0, len(data_instances)):
        attributes = strman.getKeyWords(data_instances[i])
        for j in range(0, len(attributes)):
            if cond_prob.get(attributes[j]):
                if cond_prob[attributes[j]].get(class_labels[i]):
                    cond_prob[attributes[j]][class_labels[i]] += 1
                else:
                    cond_prob[attributes[j]][class_labels[i]] = 1
            else:
                cond_prob[attributes[j]] = dict([(class_labels[i], 1)])
    for attr_key in cond_prob.keys():
        for attr_label_key in cond_prob[attr_key].keys() :
            cond_prob[attr_key][attr_label_key] /= (prior[attr_label_key]*total_data_instances)
    return cond_prob

def predict(data_instance,livelihood,prior,total_instances):
    attributes = strman.getKeyWords(data_instance)
    max_posterior = -1
    max_posterior_label = ''
    for label in prior.keys() :
        posterior = prior[label]
        for i in range(0,len(attributes)):
            if livelihood.get(attributes[i]):
                if livelihood[attributes[i]].get(label):
                    posterior *= livelihood[attributes[i]][label]
                else:
                    posterior *= (1/((prior[label]*total_instances)+1))
            else:
                posterior *= (1 / ((prior[label] * total_instances) + 1))
        if posterior > max_posterior :
            max_posterior = posterior
            max_posterior_label = label
    return max_posterior_label

def getAccuracy(data_instances,class_labels,livelihood,prior):
    positive = 0
    total_instances = len(data_instances)
    for i in range (0,len(data_instances)):
        predicted_class = predict(data_instances[i], livelihood, prior,total_instances)
        if class_labels[i] == predicted_class :
            positive +=1
    return (positive/total_instances)*100