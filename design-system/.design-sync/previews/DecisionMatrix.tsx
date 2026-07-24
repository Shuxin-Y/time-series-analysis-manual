import React from "react";
import { DecisionMatrix } from "@tsam/design-system";

export const StationarityVerdict = () => (
  <DecisionMatrix
    headers={["ADF", "KPSS", "Verdict"]}
    rows={[
      [
        "Reject",
        "Fail to reject",
        { content: "Stationary", verdict: "good" }
      ],
      [
        "Fail to reject",
        "Reject",
        { content: "Unit root — difference", verdict: "problem" }
      ],
      [
        "Reject",
        "Reject",
        { content: "Inconclusive — inspect", verdict: "escalate" }
      ]
    ]}
  />
);
