import {
  FormLabel,
  IconButton,
  InputAdornment,
  Link,
  OutlinedInput,
} from "@mui/material";
import { Stack } from "@mui/system";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import React, { useState } from "react";
import { Logos } from "../../Assets";
import { useNavigate } from "react-router-dom";
import { CustomButton, CustomizedTextField } from "../../GlobalStyle";
import AlternateEmailIcon from "@mui/icons-material/AlternateEmail";
import LockIcon from "@mui/icons-material/Lock";
import { Visibility, VisibilityOff } from "@mui/icons-material";

const Signin = () => {
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();
  return (
    <Stack id="wrapper" height={"97%"} justifyContent="flex-end">
      <Stack id="all-except-Button" height={"100%"} spacing={5}>
        <Stack id="back-icon-and-logo" alignItems={"start"} spacing={5}>
          <IconButton
            sx={{
              padding: 0,
              marginTop: 1,
            }}
            onClick={() => navigate("/")}
          >
            <ChevronLeftIcon fontSize="large" />
          </IconButton>
          <Stack width={"100%"} alignItems={"center"}>
            <img width={148} height={65} src={Logos.medium} alt="logo" />
          </Stack>
        </Stack>

        <Stack id="text-fields" spacing={3}>
          <Stack id="Username">
            <FormLabel>Username</FormLabel>
            <CustomizedTextField
              placeholder={"Username"}
              variant="outlined"
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <AlternateEmailIcon />
                  </InputAdornment>
                ),
              }}
            />
          </Stack>
          <Stack id="password">
            <FormLabel>Password</FormLabel>
            <OutlinedInput
              id="outlined-adornment-Password"
              type={showPassword ? "text" : "password"}
              placeholder={"Password"}
              variant="outlined"
              startAdornment={
                <InputAdornment position="start">
                  <LockIcon />
                </InputAdornment>
              }
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={() => setShowPassword(!showPassword)}
                    edge="end"
                  >
                    {showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
            />
            <Link href="#" underline="none" color="secondary" marginTop="16px">
              forget password?
            </Link>
          </Stack>
        </Stack>
      </Stack>
      <Stack id="button">
        <CustomButton color="secondary" variant="contained">
          Sign In
        </CustomButton>
      </Stack>
    </Stack>
  );
};

export default Signin;
