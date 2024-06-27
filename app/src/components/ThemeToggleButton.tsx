import { Switch } from "@nextui-org/react";

import DarkModeIcon from "./DarkModeIcon";
import LightModeIcon from "./LightModeIcon";

const ThemeToggleButton = () => {
  return (
    <Switch
      size="lg"
      color="secondary"
      thumbIcon={({ isSelected }) =>
        isSelected ? <DarkModeIcon /> : <LightModeIcon />
      }
    ></Switch>
  );
};

export default ThemeToggleButton;
