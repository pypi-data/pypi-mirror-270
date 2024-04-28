import __local__
from luma.neural.network import MLP
from luma.neural.optimizer import AdamOptimizer
from luma.neural.layer import Activation
from luma.metric.classification import Accuracy

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt


X, y = load_digits(return_X_y=True)


model = MLP(
    in_features=64,
    out_features=10,
    hidden_layers=[100, 32],
    batch_size=100,
    n_epochs=100,
    learning_rate=0.001,
    dropout_rate=0.5,
    optimizer=AdamOptimizer(),
    activation=Activation.ReLU(),
    out_activation=Activation.Softmax(),
)

model.fit(X, y)
y_pred = model.predict(X)
y_score = model.score(X, y, metric=Accuracy)

plt.plot(model.train_loss_, label="Train Loss")
plt.plot(model.valid_loss_, label="Valid Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title(f"MLP Training [Acc: {y_score:.4f}]")
plt.legend()
plt.grid(alpha=0.2)

plt.tight_layout()
plt.show()
