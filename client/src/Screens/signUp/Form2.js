import {
  Autocomplete,
  Box,
  FormLabel,
  InputAdornment,
  Typography,
  useMediaQuery,
} from "@mui/material";
import BrokenImageOutlinedIcon from "@mui/icons-material/BrokenImageOutlined";
import { Stack } from "@mui/system";
import { CustomizedTextField } from "../../GlobalStyle";
import CorporateFareIcon from "@mui/icons-material/CorporateFare";
import LocalPhoneOutlinedIcon from "@mui/icons-material/LocalPhoneOutlined";

const Form2 = ({ register, errors }) => {
  const matches = useMediaQuery("(min-height:670px)");
  const categories = ["super market", "resturant"];
  return (
    <Stack id="text-fields" spacing={3}>
      <Stack id="businessName">
        <FormLabel error={errors.businessName ? true : false}>
          {errors.businessName ? errors.businessName.message : "Business name"}
        </FormLabel>
        <CustomizedTextField
          placeholder={"businessName"}
          type={"text"}
          variant="outlined"
          error={errors.businessName ? true : false}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <CorporateFareIcon />
              </InputAdornment>
            ),
          }}
          {...register("businessName")}
        />
      </Stack>
      <Stack id="phoneNumber">
        <FormLabel error={errors.phoneNumber ? true : false}>
          {errors.phoneNumber ? errors.phoneNumber.message : "Phone number"}
        </FormLabel>
        <CustomizedTextField
          type={"tel"}
          placeholder={"number"}
          variant="outlined"
          error={errors.phoneNumber ? true : false}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <LocalPhoneOutlinedIcon />
              </InputAdornment>
            ),
          }}
          {...register("phoneNumber")}
        />
      </Stack>
      <Stack>
        <FormLabel error={errors.businessCatagory ? true : false}>
          {errors.businessCatagory
            ? errors.businessCatagory.message
            : "Category / industry"}
        </FormLabel>
        <Autocomplete
          disablePortal
          id="combo-box-demo"
          options={categories}
          renderInput={(params) => (
            <CustomizedTextField
              placeholder="Select Category / industry"
              {...params}
              {...register("businessCatagory")}
            />
          )}
        />
      </Stack>
      <Box
        component={"label"}
        bgcolor="rgba(240, 133, 11, 0.05)"
        justifyContent={"center"}
        alignItems="center"
        sx={{
          display: "flex",
          flexDirection: "column",
          cursor: "pointer",
          border: "1px dashed #F0850B",
          borderRadius: "4px",
          height: matches ? "140px" : "80px",
        }}
      >
        <BrokenImageOutlinedIcon
          sx={{
            fill: " #F0850B",
          }}
          fontSize="large"
        />
        <Typography fontSize={"12px"} fontWeight={500}>
          Upload logo here
        </Typography>
        <input hidden accept="image/*" type="file" {...register("logo")} />
      </Box>
    </Stack>
  );
};

export default Form2;
