def call():
    content = input("Enter what you want")
    if content == 'bayes':
        bayes = '''      X_train = np.array([
                        [2, 1, 3, 0, 0, 1],
                        [1, 1, 1, 0, 0, 0],
                        [1, 1, 2, 0, 1, 0],
                        [0, 1, 0, 2, 1, 1],
                        [0, 0, 1, 1, 1, 0],
                        [0, 0, 0, 2, 2, 0]
                    ])
                    y_train = np.array(['Terrorism', 'Terrorism', 'Terrorism', 'Entertainment', 'Entertainment', 'Entertainment'])
        
        
                    class_labels = np.unique(y_train)
                    array(['Entertainment', 'Terrorism'], dtype='<U13')
        
                    # Prior probabilities
                    prior_prob = {}
                    for label in class_labels:
                        prior_prob[label] = np.sum(y_train == label) / len(y_train)
        
                    prior_prob
                    {'Entertainment': 0.5, 'Terrorism': 0.5}
        
                    # Conditional probabilities
                    conditional_prob = {}
                    for label in class_labels:
                        conditional_prob[label] = np.round((X_train[y_train == label].sum(axis=0) + 1) / (np.sum(X_train[y_train == label]) + X_train.shape[1]),4)
        
                    conditional_prob
                    {'Entertainment': array([0.0556, 0.1111, 0.1111, 0.3333, 0.2778, 0.1111]),
                    'Terrorism': array([0.2381, 0.1905, 0.3333, 0.0476, 0.0952, 0.0952])}
        
                    X_test = np.array([[1, 1, 1, 1, 1, 1]])
        
                    def predict(X):
                        predictions = []
                        for i in range(X.shape[0]):
                            probs = {}
                            for label in class_labels:
                                likelihood = np.prod(conditional_prob[label] ** X[i]) * prior_prob[label]
                                probs[label] = likelihood
                            prediction = max(probs, key=probs.get)
                            predictions.append(prediction)
                        return predictions
        
        
                    predicted_class = predict(X_test)
                    print("Predicted class:", predicted_class[0])
                    #Predicted class: Entertainment
        
        
        
                    import requests
                    import zipfile
                    import pandas as pd
        
                    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'
                    data_file = 'SMSSpamCollection'
        
                    # Make request
                    resp = requests.get(url)
        
                    # Get filename
                    filename = url.split('/')[-1]
        
                    # Download zipfile
                    with open(filename, 'wb') as f:
                    f.write(resp.content)
        
                    # Extract Zip
                    with zipfile.ZipFile(filename, 'r') as zip:
                    zip.extractall('')
        
                    # Read Dataset
                    data = pd.read_table(data_file,
                                        header = 0,
                                        names = ['type', 'message']
                                        )
        
                    # Show dataset
                    data.head()
        
                    type	message
                    0	ham	Ok lar... Joking wif u oni...
                    1	spam	Free entry in 2 a wkly comp to win FA Cup fina...
                    2	ham	U dun say so early hor... U c already then say...
                    3	ham	Nah I don't think he goes to usf, he lives aro...
                    4	spam	FreeMsg Hey there darling it's been 3 week's n...
        
        
                    from sklearn.feature_extraction.text import CountVectorizer
                    vectorizer = CountVectorizer()
                    X = vectorizer.fit_transform(data['message'])
                    y = data['type']
        
                    from sklearn.model_selection import train_test_split
        
                    # Assuming your feature matrix is in 'X' and labels are in a variable 'y'
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
                    X_train_arr = X_train.toarray()
                    # y_train_arr = y_train.toarray()
        
                    from sklearn.naive_bayes import GaussianNB
        
                    # Create the model
                    model = GaussianNB()
        
                    # Fit (train) the model
                    model.fit(X_train.toarray(), y_train)
        
                    y_pred = model.predict(X_test.toarray())
        
                    from sklearn.metrics import accuracy_score, confusion_matrix
        
                    accuracy = accuracy_score(y_test, y_pred)
                    cm = confusion_matrix(y_test, y_pred)
        
                    print("Accuracy:", accuracy)
                    print("Confusion Matrix:\n", cm)
        
                    from sklearn.naive_bayes import MultinomialNB
        
                    model = MultinomialNB()
                    model.fit(X_train, y_train)  # No need to convert to a dense matrix
        
        
                    y_pred = model.predict(X_test)
        
                    from sklearn.metrics import accuracy_score, confusion_matrix
        
                    accuracy = accuracy_score(y_test, y_pred)
                    cm = confusion_matrix(y_test, y_pred)
        
                    print("Accuracy:", accuracy)
                    print("Confusion Matrix:\n", cm)
        
        
                    from sklearn.naive_bayes import BernoulliNB
        
                    model = BernoulliNB()
        
                    # 4. Fit the Model
                    model.fit(X_train, y_train)
        
                    # 5. Evaluation: Predictions
                    y_pred_train = model.predict(X_train_arr)
                    y_pred_test = model.predict(X_test.toarray())
        
                    # 6. Evaluation: Accuracy
                    accuracy_train = accuracy_score(y_train, y_pred_train)
                    accuracy_test = accuracy_score(y_test, y_pred_test)
        
                    print("Training Accuracy:", accuracy_train)
                    print("Testing Accuracy:", accuracy_test)
        
                    # 7. Evaluation: Confusion Matrices
                    cm_train = confusion_matrix(y_train, y_pred_train)
                    cm_test = confusion_matrix(y_test, y_pred_test)
        
                    print("Training Confusion Matrix:\n", cm_train)
                    print("Testing Confusion Matrix:\n", cm_test)'''
        return print(bayes)
        
    elif (content == 'linear'):
        linear = '''X=np.array([1,2,3,4,5,6,7,8,9]);
        y=np.array([2,3,5,8,10,11,14,17,18]);
        df=pd.DataFrame({
            'X':X,
            'y':y
        })
            
        xmean = np.mean(X)
        ymean = np.mean(y)
        
        df['xycov']=(df['X']-xmean) * (df['y']-ymean)
        df['xvar']=(df['X']-xmean)**2
        
        B1 = df['xycov'].sum()/df['xvar'].sum()
        
        B0 = ymean - ( B1 * xmean)
        
        y_pred = B0 + (B1 * np.array(X))
        
        mse = (y - y_pred)**2
        
        mse = np.mean((y - y_pred)**2)
        mse
        
        b0_initial = 0;
        b1_initial = 0;
        
        iterations=1000;
        learning_rate = 0.01;
        
        def gradient_descent(x,y,b0,b1,learning_rate,iterations):
        n=len(x)
        for i in range(iterations):
            y_pred2=b0+b1*x
        
            grad_b0 = (-2/n)* np.sum(y-y_pred2)
            grad_b1 = (-2/n)* np.sum(x*(y-y_pred2))
        
            b0 -= learning_rate * grad_b0
            b1 -= learning_rate * grad_b1
        
        
            if(i % 100 ==0):
            mse=np.mean((y-y_pred2)**2)
            print(f"iteration mse {i}, MSE:{mse}")
        
        return b0,b1
        
        b0_final,b1_final = gradient_descent(X,y,b0_initial,b1_initial,learning_rate,iterations)
        print("final coeffient",b0_final,b1_final)
        
        
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        model.fit(X.reshape(-1,1),y)
        
        a=[[7]]
        b=[14]
        y_pred=model.predict(a)
        
        from sklearn.metrics import mean_squared_error
        
        y_pred2=model.predict(X.reshape(-1,1))
        
        
        mse = mean_squared_error(y,y_pred2)
        
        from sklearn.linear_model import SGDRegressor
        GD=SGDRegressor(max_iter=1000,tol=0.01,random_state=42)
        GD.fit(X.reshape(-1,1),y)
        
        
        GD_pred=GD.predict(X.reshape(-1,1))
        
        mse=mean_squared_error(y,GD_pred)'''
        return print(linear)
    elif(content == 'KNNandSVM'):
        KNNandSVM = ''' import numpy as np
        class KNN:
        def __init__(self, k):
        self.k = k
        
        def fit(self,X_train,y_train):
        self.X_train=X_train
        self.y_train=y_train
        
        def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))
        
        def predict(self,X_test):
        y_pred = [self._predict(x) for x in X_test]
        return np.array(y_pred)
        
        def _predict(self, x):
        distances = [self.euclidean_distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = np.bincount(k_nearest_labels).argmax()
        return most_common
        
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import accuracy_score, confusion_matrix
        from sklearn.model_selection import train_test_split
        
        plt.figure(figsize=(8,8))
        sns.scatterplot(x=plot_data['Feature-1'],y=plot_data['Feature-2'])
        plt.title("Scatter Plot")
        plt.show()
        
        
        knn_model = KNeighborsClassifier(n_neighbors=3)
        
        
        from sklearn.datasets import load_iris
        
        iris = load_iris()
        X = iris.data[:, :2]
        y = iris.target
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Sepal Width (cm)')
        plt.title('Scatterplot of Iris Data Points')
        plt.show()
        
        
        from sklearn import datasets
        from sklearn.model_selection import train_test_split
        from sklearn.svm import SVC
        from sklearn.metrics import accuracy_score, confusion_matrix
        
        iris = datasets.load_iris()
        X = iris.data
        y = iris.target
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # SVM with Linear Kernel
        svm_linear = SVC(kernel='linear')
        svm_linear.fit(X_train, y_train)
        
        y_pred_train_linear = svm_linear.predict(X_train)
        y_pred_test_linear = svm_linear.predict(X_test)
        
        accuracy_train_linear = accuracy_score(y_train, y_pred_train_linear)
        accuracy_test_linear = accuracy_score(y_test, y_pred_test_linear)
        
        confusion_matrix_train_linear = confusion_matrix(y_train, y_pred_train_linear)
        confusion_matrix_test_linear = confusion_matrix(y_test, y_pred_test_linear)
        
        print("Linear Kernel:")
        print(f"Training Accuracy: {accuracy_train_linear}")
        print(f"Testing Accuracy: {accuracy_test_linear}")
        print("Confusion Matrix (Training):\n", confusion_matrix_train_linear)
        print("Confusion Matrix (Testing):\n", confusion_matrix_test_linear)
        print("\n")
        
        # SVM with Polynomial Kernel
        svm_poly = SVC(kernel='poly', degree=3)
        svm_poly.fit(X_train, y_train)
        
        y_pred_train_poly = svm_poly.predict(X_train)
        y_pred_test_poly = svm_poly.predict(X_test)
        
        accuracy_train_poly = accuracy_score(y_train, y_pred_train_poly)
        accuracy_test_poly = accuracy_score(y_test, y_pred_test_poly)
        
        confusion_matrix_train_poly = confusion_matrix(y_train, y_pred_train_poly)
        confusion_matrix_test_poly = confusion_matrix(y_test, y_pred_test_poly)
        
        print("Polynomial Kernel:")
        print(f"Training Accuracy: {accuracy_train_poly}")
        print(f"Testing Accuracy: {accuracy_test_poly}")
        print("Confusion Matrix (Training):\n", confusion_matrix_train_poly)
        print("Confusion Matrix (Testing):\n", confusion_matrix_test_poly)
        print("\n")
        
        # SVM with RBF Kernel
        svm_rbf = SVC(kernel='rbf')
        svm_rbf.fit(X_train, y_train)
        
        y_pred_train_rbf = svm_rbf.predict(X_train)
        y_pred_test_rbf = svm_rbf.predict(X_test)
        
        accuracy_train_rbf = accuracy_score(y_train, y_pred_train_rbf)
        accuracy_test_rbf = accuracy_score(y_test, y_pred_test_rbf)
        
        confusion_matrix_train_rbf = confusion_matrix(y_train, y_pred_train_rbf)
        confusion_matrix_test_rbf = confusion_matrix(y_test, y_pred_test_rbf)
        
        print("RBF Kernel:")
        print(f"Training Accuracy: {accuracy_train_rbf}")
        print(f"Testing Accuracy: {accuracy_test_rbf}")
        print("Confusion Matrix (Training):\n", confusion_matrix_train_rbf)
        print("Confusion Matrix (Testing):\n", confusion_matrix_test_rbf)
        
        
        from sklearn.datasets import make_moons
        
        X_moons, y_moons = make_moons(n_samples=1000, noise=0.3, random_state=42)
        
        plt.scatter(X_moons[:, 0], X_moons[:, 1], c=y_moons, cmap='viridis', marker='o')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title('Scatterplot of Moon-shaped Data Points')
        plt.show()
        
        
        
        
        from sklearn.datasets import make_moons
        from sklearn.model_selection import train_test_split
        from sklearn.svm import SVC
        from sklearn.metrics import accuracy_score, confusion_matrix
        import matplotlib.pyplot as plt
        
        X_moons, y_moons = make_moons(n_samples=1000, noise=0.3, random_state=42)
        
        X_train, X_test, y_train, y_test = train_test_split(X_moons, y_moons, test_size=0.2, random_state=42)
        
        # SVM with Linear Kernel
        svm_linear = SVC(kernel='linear')
        svm_linear.fit(X_train, y_train)
        
        
        y_pred_train_linear = svm_linear.predict(X_train)
        y_pred_test_linear = svm_linear.predict(X_test)
        
        
        accuracy_train_linear = accuracy_score(y_train, y_pred_train_linear)
        accuracy_test_linear = accuracy_score(y_test, y_pred_test_linear)
        
        confusion_matrix_train_linear = confusion_matrix(y_train, y_pred_train_linear)
        confusion_matrix_test_linear = confusion_matrix(y_test, y_pred_test_linear)
        
        print("Linear Kernel:")
        print(f"Training Accuracy: {accuracy_train_linear}")
        print(f"Testing Accuracy: {accuracy_test_linear}")
        print("Confusion Matrix (Training):\n", confusion_matrix_train_linear)
        print("Confusion Matrix (Testing):\n", confusion_matrix_test_linear)
        print("\n")
        
        
        svm_poly = SVC(kernel='poly', degree=3)
        svm_poly.fit(X_train, y_train)
        
        
        y_pred_train_poly = svm_poly.predict(X_train)
        y_pred_test_poly = svm_poly.predict(X_test)
        
        
        accuracy_train_poly = accuracy_score(y_train, y_pred_train_poly)
        accuracy_test_poly = accuracy_score(y_test, y_pred_test_poly)
        
        confusion_matrix_train_poly = confusion_matrix(y_train, y_pred_train_poly)
        confusion_matrix_test_poly = confusion_matrix(y_test, y_pred_test_poly)
        
        print("Polynomial Kernel:")
        print(f"Training Accuracy: {accuracy_train_poly}")
        print(f"Testing Accuracy: {accuracy_test_poly}")
        print("Confusion Matrix (Training):\n", confusion_matrix_train_poly)
        print("Confusion Matrix (Testing):\n", confusion_matrix_test_poly)
        print("\n")
        
        svm_rbf = SVC(kernel='rbf')
        svm_rbf.fit(X_train, y_train)
        
        y_pred_train_rbf = svm_rbf.predict(X_train)
        y_pred_test_rbf = svm_rbf.predict(X_test)
        
        accuracy_train_rbf = accuracy_score(y_train, y_pred_train_rbf)
        accuracy_test_rbf = accuracy_score(y_test, y_pred_test_rbf)
        
        confusion_matrix_train_rbf = confusion_matrix(y_train, y_pred_train_rbf)
        confusion_matrix_test_rbf = confusion_matrix(y_test, y_pred_test_rbf)
        
        print("RBF Kernel:")
        print(f"Training Accuracy: {accuracy_train_rbf}")
        print(f"Testing Accuracy: {accuracy_test_rbf}")
        print("Confusion Matrix (Training):\n", confusion_matrix_train_rbf)
        print("Confusion Matrix (Testing):\n", confusion_matrix_test_rbf)
        print("\n")'''
        return print(KNNandSVM)
    elif(content=='Pipeline'):
        Pipeline ='''from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.model_selection import cross_val_score
        log_reg_pipeline = Pipeline([
            ('scaler',StandardScaler()),
            ('classifier',LogisticRegression())
        ])
        
        knn_pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', KNeighborsClassifier())
        ])
        
        dt_pipeline = Pipeline([
            ('classifier', DecisionTreeClassifier())
        ])
        
        nb_pipeline = Pipeline([
            ('classifier', GaussianNB())
        ])
        
        mlp_pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', MLPClassifier())
        ])
        
        models = {
            'Logistic Regression': log_reg_pipeline,
            'KNN Classifier': knn_pipeline,
            'SVM CLassifier': svm_pipeline,
            'Decision Tree Classifier': dt_pipeline,
            'Multilayer Perceptron': mlp_pipeline,
            'Naive Bayes Classfier': nb_pipeline
        }
        
        for name, model in models.items():
            scores = cross_val_score(model, X, y, cv=5)
            print(f'{name}: Mean Accuracy = {scores.mean():.4f}, Std Dev = {scores.std():.4f}')'''
        return print(Pipeline)
    elif(content=='Week8'):
        Week8='''from sklearn.ensemble import BaggingClassifier
        
        BC_model = BaggingClassifier(n_estimators=100, random_state=42)
        
        BC_model.fit(X_train,y_train)
        
        y_pred_BC=BC_model.predict(X_test)
        
        accuracy_BC = accuracy_score(y_test,y_pred_BC)
        
        print(f'The accuracy of the BaggingClassifier is: {accuracy_BC}')
        
        from sklearn.ensemble import BaggingClassifier
        from sklearn.neighbors import KNeighborsClassifier
        
        BG_Knn_model = BaggingClassifier(base_estimator=KNeighborsClassifier() , n_estimators=100, random_state=42)
        
        BG_Knn_model.fit(X_train,y_train)
        
        y_pred_BG_Knn = BG_Knn_model.predict(X_test)
        
        accuracy_BG_Knn=accuracy_score(y_test,y_pred_BG_Knn)
        
        print(f'The accuracy of the  Bagged K-Nearest Neighbors is: {accuracy_BG_Knn}')
        
        from sklearn.ensemble import GradientBoostingClassifier
        
        GBC_model = GradientBoostingClassifier(n_estimators=300, learning_rate=0.05,random_state=100)
        
        
        # Fit to training set
        GBC_model.fit(X_train, y_train)
        
        # Predict on test set
        y_pred_GBC = GBC_model.predict(X_test)
        
        # accuracy
        acc = accuracy_score(y_test,y_pred_GBC)
        print(f'Gradient Boosting Classifier accuracy is : {acc}')
        from sklearn.ensemble import AdaBoostClassifier
        
        ABC_model = AdaBoostClassifier(n_estimators=100, random_state=42)
        
        ABC_model.fit(X_train,y_train)
        
        y_pred_ABC=ABC_model.predict(X_test)
        
        accuracy_ABC=accuracy_score(y_test,y_pred_ABC)
        print(f'AdaBoostClassifier accuracy is : {accuracy_ABC}')
        
        import xgboost as xgb
        
        xg = xgb.XGBClassifier(n_estimators=100, random_state=42)
        
        
        xg.fit(X_train, y_train)
        
        
        y_pred_xg = xg.predict(X_test)
        
        
        accuracy_xg = accuracy_score(y_test, y_pred_xg)
        
        print(f'The accuracy of the XGBoost on the test set is: {accuracy_xg}')
        
        
        from sklearn.ensemble import VotingClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn.svm import SVC
        
        vc = VotingClassifier(estimators=[('lr', LogisticRegression()), ('svc', SVC())], voting='hard')
        
        
        vc.fit(X_train, y_train)
        
        
        y_pred_vc = vc.predict(X_test)
        
        
        accuracy_vc = accuracy_score(y_test, y_pred_vc)
        
        print(f'The accuracy of the Voting Classifier on the test set is: {accuracy_vc}')
        
        
        import numpy as np
        
        y_pred1 = DT_model.predict_proba(X_test)
        y_pred2 = Rf_model.predict_proba(X_test)
        y_pred3 = BC_model.predict_proba(X_test)
        
        
        weights = np.array([0.2, 0.3, 0.5])
        
        y_pred_wa = weights[0] * y_pred1 + weights[1] * y_pred2 + weights[2] * y_pred3
        
        
        y_pred_wa = np.argmax(y_pred_wa, axis=1)
        
        
        accuracy_wa = accuracy_score(y_test, y_pred_wa)
        
        print(f'The accuracy of the Weighted Average on the test set is: {accuracy_wa}')
        
        from sklearn.model_selection import train_test_split
        
        X_train_new, X_val, y_train_new, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
        
        DT_model.fit(X_train_new, y_train_new)
        Rf_model.fit(X_train_new, y_train_new)
        
        # Make predictions on the validation set
        val_pred1 = DT_model.predict(X_val)
        val_pred2 = Rf_model.predict(X_val)
        
        # Stack predictions
        stacked_predictions = np.column_stack((val_pred1, val_pred2))
        
        # Train a meta-classifier on the stacked predictions
        meta_clf = LogisticRegression()
        meta_clf.fit(stacked_predictions, y_val)
        
        # Make predictions on the test set using the trained classifiers
        test_pred1 = DT_model.predict(X_test)
        test_pred2 = Rf_model.predict(X_test)
        
        # Stack predictions
        stacked_test_predictions = np.column_stack((test_pred1, test_pred2))
        
        # Make final predictions using the meta-classifier
        final_predictions = meta_clf.predict(stacked_test_predictions)
        
        # Calculate the accuracy of the classifier on the test set
        accuracy_blending = accuracy_score(y_test, final_predictions)
        
        print(f'The accuracy of the Blending on the test set is: {accuracy_blending}')'''
        
        return print(Week8)
    elif(content=='kmean'):
        kmean=''' X = np.array([2, 2, 8, 5, 7, 6, 1, 4])
                            Y = np.array([10, 5, 4, 8, 5, 4, 2, 9])
                            data = np.array(list(zip(X, Y)))

                            K = 2

                            C = data[np.random.choice(range(len(data)), size=K, replace=False)]

                            for _ in range(1):

                                labels = np.argmin(np.linalg.norm(data[:, None] - C, axis=-1), axis=-1)


                                C = np.array([data[labels == k].mean(axis=0) for k in range(K)])

                            print(f"Centroids after 1 iteration: {C}")


                            K = 3

                            C = data[np.random.choice(range(len(data)), size=K, replace=False)]

                            for _ in range(1):

                                labels = np.argmin(np.linalg.norm(data[:, None] - C, axis=-1), axis=-1)


                                C = np.array([data[labels == k].mean(axis=0) for k in range(K)])

                            print(f"Centroids after 1 iteration: {C}")
                            from sklearn.cluster import KMeans
                            import matplotlib.pyplot as plt

                            X = np.array([[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]])


                            wss = []
                            for k in range(1, 8):
                                kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
                                kmeans.fit(X)
                                wss.append(kmeans.inertia_)


                            plt.plot(range(1, 8), wss)
                            plt.title('Elbow Method')
                            plt.xlabel('Number of clusters')
                            plt.ylabel('WSS')
                            plt.show()

                            import numpy as np


                            X = np.array([2, 2, 8, 5, 7, 6, 1, 4])
                            Y = np.array([10, 5, 4, 8, 5, 4, 2, 9])
                            data = np.array(list(zip(X, Y)))


                            K = 3


                            C = data[np.random.choice(range(len(data)), size=K, replace=False)]

                            iterations = 10


                            for _ in range(iterations):

                                labels = np.argmin(np.linalg.norm(data[:, None] - C, axis=-1), axis=-1)

                                C = np.array([data[labels == k].mean(axis=0) for k in range(K)])

                            print(f"Centroids after {iterations} iterations: {C}")

                            from sklearn.metrics import silhouette_score


                            score = silhouette_score(data, labels)

                            print(f"Silhouette score: {score}")

                            import numpy as np


                            X = np.array([2, 2, 8, 5, 7, 6, 1, 4])
                            Y = np.array([10, 5, 4, 8, 5, 4, 2, 9])
                            data = np.array(list(zip(X, Y)))

                            K = 3


                            C = [data[np.random.randint(data.shape[0])]]
                            for _ in range(1, K):
                                dist = np.array([min([np.inner(c-x,c-x) for c in C]) for x in data])
                                probs = dist/dist.sum()
                                cumprobs = probs.cumsum()
                                r = np.random.rand()

                                for j,p in enumerate(cumprobs):
                                    if r < p:
                                        i = j
                                        break

                                C.append(data[i])

                            C = np.array(C)

                            iterations = 10


                            for _ in range(iterations):

                                labels = np.argmin(np.linalg.norm(data[:, None] - C, axis=-1), axis=-1)


                                C = np.array([data[labels == k].mean(axis=0) for k in range(K)])

                            print(f"Centroids after {iterations} iterations: {C}")



                            from sklearn.cluster import KMeans
                            from sklearn.metrics import silhouette_score


                            X = np.array([2, 2, 8, 5, 7, 6, 1, 4])
                            Y = np.array([10, 5, 4, 8, 5, 4, 2, 9])
                            data = np.array(list(zip(X, Y)))


                            K = 3

                            kmeans = KMeans(n_clusters=K, init='k-means++', random_state=42)
                            kmeans.fit(data)


                            C_sklearn = kmeans.cluster_centers_

                            labels_sklearn = kmeans.labels_


                            score_sklearn = silhouette_score(data, labels_sklearn)

                            print(f"Centroids after fitting KMeans: {C_sklearn}")
                            print(f"Silhouette score: {score_sklearn}")'''
        return kmean
    elif(content=='pca'):
        pca='''import seaborn as sns
                        import matplotlib.pyplot as plt

                        # Histograms for each feature
                        df.hist(figsize=(10, 8))
                        plt.tight_layout()
                        plt.show()


                        # Correlation Heatmap
                        plt.figure(figsize=(10, 8))
                        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
                        plt.title('Correlation Heatmap')
                        plt.show()

                        from sklearn.preprocessing import StandardScaler  # = StandardScaler() scaled_data = scaler.fit_transform(df)
                        from sklearn.preprocessing import StandardScaler
                        scaler = StandardScaler()
                        scaled_data = scaler.fit_transform(df)
                        scaled_data

                        from sklearn.cluster import KMeans
                        import matplotlib.pyplot as plt

                        wcss = []

                        for i in range(1, 11):
                        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
                        kmeans.fit(scaled_data)
                        wcss.append(kmeans.inertia_)

                        kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
                        kmeans.fit(scaled_data)
                        df['Kmeans_Cluster'] = kmeans.labels_

                        from sklearn.cluster import AgglomerativeClustering
                        agg = AgglomerativeClustering(n_clusters=3)
                        df['Agglomerative_Cluster'] = agg.fit_predict(scaled_data)

                        df['Cluster_Difference'] = df['Kmeans_Cluster'] - df['Agglomerative_Cluster']

                        print(df['Cluster_Difference'].value_counts())

                        from sklearn.decomposition import PCA
                        pca = PCA(n_components=2)
                        principal_components = pca.fit_transform(scaled_data)
                        principal_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

                        kmeans_pca = KMeans(n_clusters=3, init='k-means++', random_state=42)
                        kmeans_pca.fit(principal_df)

                        agg_pca = AgglomerativeClustering(n_clusters=3)

                        df['PCA_Kmeans_Cluster'] = kmeans_pca.labels_
                        df['PCA_Agglomerative_Cluster'] = agg_pca.fit_predict(principal_df)'''
        return pca
    elif(content=='week11'):
        week11='''import pandas as pd

                                # Load the dataset
                                df = pd.read_csv("/content/Supermart_Data.csv", header=None)  # Assuming there are no column names in the CSV

                                # Create an empty list to store arrays of items
                                transactions = []

                                # Iterate over each row in the DataFrame
                                for index, row in df.iterrows():
                                    # Convert the row values into a list
                                    items = list(row)
                                    # Append the list of items to the transactions list
                                    transactions.append(items)

                                # Print the first few transactions as an example
                                for i in range(5):  # Adjust the range to print desired number of transactions
                                    print(transactions[i])


                                #Display basic information about the dataset
                                print("Shape of the dataset:", df.shape)
                                print("\nFirst few rows of the dataset:")
                                print(df.head())

                                # Check for missing values
                                print("\nMissing values:")
                                print(df.isnull().sum())

                                # Analyze item frequency
                                all_items = []
                                for index, row in df.iterrows():
                                    all_items.extend(row)
                                item_counts = pd.Series(all_items).value_counts()
                                print("\nItem frequency:")
                                print(item_counts)

                                import pandas as pd
                                from mlxtend.frequent_patterns import apriori, association_rules

                                # Load the dataset
                                df = pd.read_csv("/content/Supermart_Data.csv", header=None)

                                # Convert the dataset into a list of lists format
                                transactions = df.apply(lambda x: [str(item) for item in x.dropna().values], axis=1).tolist()

                                # Convert the dataset into a one-hot encoded format using TransactionEncoder
                                from mlxtend.preprocessing import TransactionEncoder

                                te = TransactionEncoder()
                                oht_ary = te.fit_transform(transactions)
                                oht_df = pd.DataFrame(oht_ary, columns=te.columns_)

                                # Apply Apriori algorithm to find frequent patterns
                                frequent_itemsets = apriori(oht_df, min_support=0.1, use_colnames=True)

                                # Print frequent patterns
                                print("\nFrequent Patterns:")
                                print(frequent_itemsets)

                                # Apply Apriori algorithm to find strong association rules
                                association_rules_df = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

                                # Print strong association rules
                                print("\nStrong Association Rules:")
                                print(association_rules_df)'''
        return week11

        
    