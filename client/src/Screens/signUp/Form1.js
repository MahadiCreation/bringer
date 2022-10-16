import {
  FormLabel,
  IconButton,
  InputAdornment,
  OutlinedInput,
} from "@mui/material";
import { Stack } from "@mui/system";
import { useState } from "react";
import { CustomizedTextField } from "../../GlobalStyle";
import AlternateEmailIcon from "@mui/icons-material/AlternateEmail";
import MailOutlineIcon from "@mui/icons-material/MailOutline";
import LockIcon from "@mui/icons-material/Lock";
import { Visibility, VisibilityOff } from "@mui/icons-material";

const Form1 = ({ register, errors }) => {
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [showPassword, setShowPassword] = useState(false);

  return (
    <Stack id="text-fields" spacing={3}>
      <Stack id="Username">
        <FormLabel error={errors.userName ? true : false}>
          {errors.userName ? errors.userName.message : "Username"}
        </FormLabel>
        <CustomizedTextField
          type={"text"}
          placeholder={"Username"}
          variant="outlined"
          error={errors.userName ? true : false}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <AlternateEmailIcon />
              </InputAdornment>
            ),
          }}
          {...register("userName")}
        />
      </Stack>
      <Stack id="Email">
        <FormLabel error={errors.email ? true : false}>
          {errors.email ? errors.email.message : "E-mail"}
        </FormLabel>
        <CustomizedTextField
          type={"email"}
          placeholder={"E-mail"}
          variant="outlined"
          error={errors.email ? true : false}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <MailOutlineIcon />
              </InputAdornment>
            ),
          }}
          {...register("email")}
        />
      </Stack>
      <Stack id="password">
        <FormLabel error={errors.password ? true : false}>
          {errors.password ? errors.password.message : "Password"}
        </FormLabel>
        <OutlinedInput
          id="outlined-adornment-Password"
          error={errors.password ? true : false}
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
          {...register("password")}
        />
      </Stack>
      <Stack id="ConfirmPassword">
        <FormLabel error={errors.confirmPassword ? true : false}>
          {errors.confirmPassword
            ? errors.confirmPassword.message
            : "confirmPassword"}
        </FormLabel>
        <OutlinedInput
          id="outlined-adornment-ConfirmPassword"
          error={errors.confirmPassword ? true : false}
          type={showConfirmPassword ? "text" : "password"}
          placeholder={"ConfirmPassword"}
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
                onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                edge="end"
              >
                {showConfirmPassword ? <VisibilityOff /> : <Visibility />}
              </IconButton>
            </InputAdornment>
          }
          {...register("confirmPassword")}
        />
      </Stack>
    </Stack>
  );
};

export default Form1;
