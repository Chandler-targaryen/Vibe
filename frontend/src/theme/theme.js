import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    background: {
      default: "#f5f2eb"
    },
    text: {
      primary: "#000000"
    },
    primary: {
      main: "#000000"
    },
    secondary: {
      main: "#f5f2eb"
    }
  },
  typography: {
    fontFamily: "Inter, sans-serif"
  }
});

export default theme;