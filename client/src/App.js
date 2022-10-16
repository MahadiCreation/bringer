import { IntlProvider } from "react-intl";
import enMessages from "./locales/en.json";
import heMessages from "./locales/he.json";
import Container from "@mui/material/Container";
import HomePage from "./Screens/Home";
import { createTheme, ThemeProvider } from "@mui/material";
import { Routes, Route } from "react-router-dom";
import Signin from "./Screens/Signin";
import SignUp from "./Screens/signUp";

const LOCALE_MESSAGES = {
  en: enMessages,
  he: heMessages,
};


function App() {
  const theme = createTheme({
    palette: {
      secondary: {
        main: "#F0850B",
        dark: "#b75700",
      },
      grey: {
        main: "#fff",
        dark: "#ccc",
      },
    },
    components: {
      MuiFormLabel: {
        defaultProps: {
          sx: {
            color: "#1D1D1B",
            fontWeight: 600,
            fontSize: "14px",
          },
        },
      },

      MuiStepLabel: {
        defaultProps: {
          sx: {
            color: "#848894",
            fontSize: "12px",
          },
        },
      },

      MuiSvgIcon: {
        defaultProps: {
          sx: {
            fill: "#1D1D1B",
          },
        },
      },
      MuiOutlinedInput: {
        defaultProps: {
          sx: {
            border: "1px solid #e9e7e7",
          },
        },
      },
    },
  });
  const currentLocale = "en";
  return (
    <ThemeProvider theme={theme}>
      <IntlProvider
        defaultLocale="en"
        locale={currentLocale}
        messages={LOCALE_MESSAGES[currentLocale]}
      >
        <Container
          sx={{
            bgcolor: "#fff",
            height: "100vh",
          }}
          maxWidth="sm"
        >
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/signin" element={<Signin />} />
            <Route path="/signup" element={<SignUp />} />
          </Routes>
        </Container>
      </IntlProvider>
    </ThemeProvider>
  );
}

export default App;
