import numpy as np


class IteratedDiscrimAPRClassifier:

    def __init__(self):
        """

        """
        # self.classifier = mil.models.APR(step=10, verbose=0)
        self.apr = []
        self.positive_bag_indices = None
        raise Exception("Not implemented yet")

    def fit(self, x_train, y_train):
        """

        Parameters
        ----------
        x_train
        y_train
        """
        self.x_train = x_train
        self.y_train = y_train
        self.generate_apr()
        self.grow()
        print(self.apr)

    def predict_bag(self, bag):
        """

        Parameters
        ----------
        bag

        Returns
        -------

        """
        if np.all(bag >= self.apr[0]):
            if np.all(bag <= self.apr[1]):
                return 1
        return 0

    def evaluate(self, x_test, y_test):
        """

        Parameters
        ----------
        x_test
        y_test
        """
        results = np.zeros(y_test.shape)
        for i, bag in enumerate(x_test):
            result = self.predict_bag(bag)
            results[i] = result
        return results

    def generate_apr(self):

        self.positive_bag_indices = np.where(self.y_train == 1)[0]

        initial_bag_index = np.random.choice(self.positive_bag_indices)
        initial_index_instance = np.random.choice(self.x_train[initial_bag_index].shape[0])
        apr_min = apr_max = self.x_train[initial_bag_index][initial_index_instance]

        self.apr = [apr_min, apr_max]

    def grow(self):

        not_positives_bag_in_apr = []

        for bag_index in self.positive_bag_indices:
            for instance in self.x_train[bag_index]:
                if np.all(instance >= self.apr[0]) and np.all(instance <= self.apr[1]):
                    # There is already an instance of the bag in apr
                    break
            else:
                # If any instance in apr we need to get one of the bag
                not_positives_bag_in_apr.append(bag_index)

        if not not_positives_bag_in_apr:
            return

        # calculate new apr with not_positive_bag_in_apr and compare size
        new_aprs = []
        new_aprs_size = []

        for bag_index in not_positives_bag_in_apr:
            for instance in self.x_train[bag_index]:
                apr_min = np.minimum(self.apr[0], instance)
                apr_max = np.maximum(self.apr[1], instance)
                apr = (apr_min, apr_max)
                new_aprs.append(apr)
                new_aprs_size.append(self.size(apr))

        # actualizamos nuestro apr
        self.apr = new_aprs[new_aprs_size.index(min(new_aprs_size))]

    def discriminate(self):
        pass

    def size(self, apr):
        size = 0
        for i in range(self.apr[0].shape[0]):
            size += apr[1][i] - apr[0][i]
        return size
