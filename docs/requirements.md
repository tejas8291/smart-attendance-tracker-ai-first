# Requirements Specification

## Functional Requirements

### Authentication

- User can login using mobile number and password.
- User session should remain active until logout.

### Check In

- User can perform check-in.
- System should capture:
  - Latitude
  - Longitude
  - Timestamp

### Location Tracking

- System should capture user location every 15 minutes.
- Location data should be stored locally if internet is unavailable.

### Offline Support

- Location updates should be stored in local database.
- Pending records should be synchronized automatically when internet becomes available.

### Check Out

- User can perform check-out.
- Final location and timestamp should be recorded.

### Attendance History

- User can view previous attendance records.

---

## Non-Functional Requirements

### Performance

- App should launch within 3 seconds.
- Location tracking should have minimal battery impact.

### Reliability

- No attendance records should be lost during offline usage.

### Security

- APIs must require authentication token.
- Sensitive data should not be stored in plain text.

## Geo-QR Attendance

- Each workplace/location will have a unique QR code.
- User must scan QR code before check-in.
- App will capture current latitude and longitude.
- Backend will verify whether user is within 100 meters of the assigned QR location.
- If user is outside the allowed radius, attendance will not be marked.
- If internet is unavailable, scan and location data will be stored locally and synced later.

### Scalability

- Backend should support multiple users and location updates.

---

## Success Criteria

- User can login.
- User can check-in.
- Location is captured every 15 minutes.
- Offline data sync works correctly.
- User can check-out.
- Attendance history is available.
