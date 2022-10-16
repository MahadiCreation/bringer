import { IconButton } from "@mui/material";
import { Stack } from "@mui/system";
import React, { useEffect, useState } from "react";
import { Logos } from "../../Assets";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import { useNavigate } from "react-router-dom";
import { CustomButton } from "../../GlobalStyle";
import CustomizedSteppers from "../../components/Stepper";
import Form1 from "./Form1";
import Form2 from "./Form2";
import { yupResolver } from "@hookform/resolvers/yup";
import { useForm } from "react-hook-form";
import * as yup from "yup";

const schema = yup.object({
  userName: yup.string().required(),
  email: yup.string().email().required(),
  password: yup
    .string()
    .required()
    .matches(
      /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/,
      "Capital and small, number and special charechter @#$"
    ),
  confirmPassword: yup
    .string()
    .required()
    .oneOf([yup.ref("password"), null], "password didnt match"),
  businessName: yup.string().required(),
  businessCatagory: yup.string(),
  phoneNumber: yup.string().required(),
  logo: yup.mixed(),
});

const SignUp = () => {
  const navigate = useNavigate();
  const [step, setStep] = useState(false);
  const [page, setPage] = useState(false);

  const {
    register,
    handleSubmit,
    reset,
    trigger,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
  });

  const onSubmit = (data) => {
    console.log(data);
    reset();
  };

  const renderPage = (pageNumber) => {
    switch (pageNumber) {
      case false:
        return <Form1 errors={errors} register={register} />;
      case true:
        return <Form2 errors={errors} register={register} />;
    }
  };

  const handleClick = async () => {
    const triggerResult = await trigger([
      "userName",
      "password",
      "confirmPassword",
      "email",
    ]);
    if (triggerResult) {
      setStep(!step);
      setPage(!page);
    }
  };

  return (
    <Stack id="wrapper" height={"90%"} justifyContent="flex-end">
      <form
        onSubmit={handleSubmit(onSubmit)}
        style={{
          height: "100%",
        }}
      >
        <Stack height={"100%"} id="all-except-Button" spacing={5}>
          <Stack
            id="back-icon-and-logo"
            justifyContent={"space-between"}
            alignItems={"center"}
            direction="row"
          >
            <IconButton
              sx={{
                padding: 0,
              }}
              onClick={() => navigate("/")}
            >
              <ChevronLeftIcon fontSize="large" />
            </IconButton>
            <Stack>
              <img width={77} height={35} src={Logos.small} alt="logo" />
            </Stack>
          </Stack>
          <CustomizedSteppers next={step} />
          {renderPage(page)}
        </Stack>

        <Stack direction={"row"} id="button" spacing={2}>
          <CustomButton
            onClick={handleClick}
            color="secondary"
            variant="contained"
            width={page ? "50%" : "100%"}
          >
            {page ? "Back" : "Next"}
          </CustomButton>
          {page && (
            <CustomButton
              type="submit"
              color="secondary"
              variant="contained"
              width={"50%"}
            >
              submit
            </CustomButton>
          )}
        </Stack>
      </form>
    </Stack>
  );
};

export default SignUp;
