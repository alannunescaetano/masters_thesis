IF OBJECT_ID(N'[__EFMigrationsHistory]') IS NULL
BEGIN
    CREATE TABLE [__EFMigrationsHistory] (
        [MigrationId] nvarchar(150) NOT NULL,
        [ProductVersion] nvarchar(32) NOT NULL,
        CONSTRAINT [PK___EFMigrationsHistory] PRIMARY KEY ([MigrationId])
    );
END;
GO

BEGIN TRANSACTION;
GO

CREATE TABLE [Routes] (
    [Id] int NOT NULL IDENTITY,
    [ImageUrl] nvarchar(max) NOT NULL,
    [Lat] float NOT NULL,
    [Lon] float NOT NULL,
    CONSTRAINT [PK_Routes] PRIMARY KEY ([Id])
);
GO

CREATE TABLE [Answers] (
    [Id] int NOT NULL IDENTITY,
    [RouteId] int NOT NULL,
    [CyclePathExists] bit NOT NULL,
    [StreetType] int NOT NULL,
    [PavementType] int NOT NULL,
    [PavementDefectExists] bit NOT NULL,
    [CyclistPerception] int NOT NULL,
    CONSTRAINT [PK_Answers] PRIMARY KEY ([Id]),
    CONSTRAINT [FK_Answers_Routes_RouteId] FOREIGN KEY ([RouteId]) REFERENCES [Routes] ([Id]) ON DELETE CASCADE
);
GO

CREATE INDEX [IX_Answers_RouteId] ON [Answers] ([RouteId]);
GO

INSERT INTO [__EFMigrationsHistory] ([MigrationId], [ProductVersion])
VALUES (N'20230319113619_Initial', N'6.0.15');
GO

COMMIT;
GO

