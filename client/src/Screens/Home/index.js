import { Typography } from "@mui/material";
import { Stack } from "@mui/system";
import { Logos } from "../../Assets";
import { CustomButton } from "../../GlobalStyle";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();
  return (
    <Stack height={"97%"} justifyContent="flex-end">
      <Stack
        height={"100%"}
        alignItems={"center"}
        justifyContent="center"
        spacing={2}
      >
        <img src={Logos.main} alt="logo" />
        <Typography fontWeight={500} color="#004C8C">
          Delivery made easy.
        </Typography>
      </Stack>

      <Stack alignItems={"center"} spacing={2}>
        <CustomButton
          onClick={() => navigate("/signin")}
          color="secondary"
          variant="contained"
        >
          Sign In
        </CustomButton>
        <CustomButton
          boxshadow={"0px 4px 12px rgba(0, 0, 0, 0.05)"}
          border={"1px solid #e9e7e7"}
          color="grey"
          textcolor="#1D1D1B"
          variant="contained"
          onClick={() => navigate("/signup")}
        >
          Sign Up
        </CustomButton>
      </Stack>
    </Stack>
  );
};

export default HomePage;
