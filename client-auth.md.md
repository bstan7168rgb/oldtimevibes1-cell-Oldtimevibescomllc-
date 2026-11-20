<br />

Certain Google Play services (such as Google Sign-in and App Invites) require
you to provide the SHA-1 of your signing certificate so we can create an OAuth2
client and API key for your app.

## Play App Signing

If you've published your app using
[Play App Signing](https://developer.android.com/studio/publish/app-signing#app-signing-google-play),
a requirement when using
[Android App Bundle](https://developer.android.com/platform/technology/app-bundle),
you can get your SHA-1 from the
[Google Play Console](https://developer.android.com/studio/publish/app-signing#api-providers)
on the **Release \> Setup \> App Integrity** page.

## Self-sign your application

If you're not using Play App Signing, follow the instructions in the following
sections to use Keytool or Gradle's Signing Report to get your SHA-1.

### Keytool on the certificate

Open a terminal and run the `keytool` utility provided with Java to get the
SHA-1 fingerprint of the certificate. You should get both the release and debug
certificate fingerprints.

To get the release certificate fingerprint:

    keytool -list -v \
    -alias <your-key-name> -keystore <path-to-production-keystore>

To get the debug certificate fingerprint:
Mac/Linux

```
keytool -list -v \
-alias androiddebugkey -keystore ~/.android/debug.keystore
    
```
Windows

```
keytool -list -v \
-alias androiddebugkey -keystore %USERPROFILE%\.android\debug.keystore
    
```

The keytool utility prompts you to enter a password for the keystore. The
default password for the debug keystore is `android`. The keytool then prints
the fingerprint to the terminal. For example:

    Certificate fingerprint: SHA1: DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09

> [!NOTE]
> **Note:** When using Play App Signing, the upload key certificate will be different than the app signing key certificate.

### Keytool on an APK or AAB

To get the certificate of an application binary:

```bash
# APK file
keytool -printcert -jarfile app.apk
# AAB file
keytool -printcert -jarfile app.aab
```

> [!NOTE]
> **Note:** When using Play App Signing, the signature of the binary signed by the upload key certificate will be different than the binary distributed by Google Play.

### Gradle's signing report

You can also get the SHA-1 of your signing certificate using the Gradle
`signingReport` command:

    ./gradlew signingReport

The signing report will include the signing information for each of your app's
variants:

    > Task :app:signingReport
    Variant: debug
    Config: debug
    Store: ~/.android/debug.keystore
    Alias: AndroidDebugKey
    MD5: A5:88:41:04:8D:06:71:6D:FE:33:76:87:AC:AD:19:23
    SHA1: A7:89:E5:05:C8:17:A1:22:EA:90:6E:A6:EA:A3:D4:8B:3A:30:AB:18
    SHA-256: 05:A2:2C:35:EE:F2:51:23:72:4D:72:67:A5:6C:8C:58:22:2A:00:D6:DB:F6:45:D5:C1:82:D2:80:A4:69:A8:FE
    Valid until: Wednesday, August 10, 2044

To learn more about digital signing on Android, see
[Signing Your Applications](https://developer.android.com/tools/publishing/app-signing.html).