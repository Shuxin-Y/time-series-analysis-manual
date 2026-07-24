import React from "react";
import { Card, Button } from "@tsam/design-system";

export const Basic = () => (
  <Card>
    A stationary series has a constant mean and variance over time. The
    augmented Dickey–Fuller test rejects the unit-root null when the statistic
    falls below the critical value.
  </Card>
);

export const WithTitle = () => (
  <Card title="Model summary">
    ARIMA(1,1,1) fit on monthly log-returns. AIC = 412.6, log-likelihood
    = −203.3. Residuals pass the Ljung–Box test at lag 12.
  </Card>
);

export const WithAction = () => (
  <Card title="Backtest complete">
    <p style={{ marginTop: 0 }}>
      Walk-forward validation over 24 folds. Mean absolute error 3.1%.
    </p>
    <Button variant="secondary" size="sm">
      View folds
    </Button>
  </Card>
);
