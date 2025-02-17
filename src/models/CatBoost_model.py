from catboost import CatBoostRegressor
from ._models import RMSELoss

class CatBoost:

    def __init__(self, args, data):
        super().__init__()

        self.criterion = RMSELoss()

        self.X_train = data['X_train']
        self.y_train = data['y_train']
        self.X_valid = data['X_valid']
        self.y_valid = data['y_valid']
        self.sub = data['sub']
        self.cat_features = list(range(0, self.X_train.shape[1]))

        self.epochs = args.EPOCHS
        self.learning_rate = args.LR
        self.seed = args.SEED

        self.model = CatBoostRegressor(iterations=self.epochs, depth=6, learning_rate=self.learning_rate, random_seed=self.seed,  
            verbose=50)


    def train(self):
      # model: type, optimizer: torch.optim, train_dataloader: DataLoader, criterion: torch.nn, device: str, log_interval: int=100
        self.model.fit(
            self.X_train, self.y_train,
            cat_features=self.cat_features,
            eval_set=(self.X_valid, self.y_valid),
        )


    def predict_train(self):
        return self.model.get_best_score()


    def predict(self):
        predicts = self.model.predict(self.sub)
        print(self.model.get_all_params)
        return predicts