import React from "react";
import { Heading } from "@tsam/design-system";

export const Levels = () => (
  <div>
    <Heading level={1}>Stationarity and Unit Roots</Heading>
    <Heading level={2}>The Augmented Dickey–Fuller Test</Heading>
    <Heading level={3}>Choosing the lag order</Heading>
    <Heading level={4}>Information criteria</Heading>
  </div>
);

export const ChapterOpener = () => (
  <Heading level={1}>Frequency-Domain Analysis</Heading>
);

export const Section = () => (
  <Heading level={2}>Spectral density estimation</Heading>
);
